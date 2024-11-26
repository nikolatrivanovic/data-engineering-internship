import boto3
import sys
import pandas as pd
import json
from io import StringIO
import requests
from botocore.exceptions import ClientError
import re
from concurrent.futures import ThreadPoolExecutor, as_completed


class Boto3ClientSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Boto3ClientSingleton, cls).__new__(cls)
            cls._instance.session = boto3.Session(
                aws_access_key_id=sys.argv[1],
                aws_secret_access_key=sys.argv[2],
                aws_session_token=sys.argv[3],
                region_name=kwargs.get('region_name', 'eu-west-1')
            )
        return cls._instance

    def client(self, service_name):
        return self.session.client(service_name)


BUCKET_NAME = "processed-data-levi9-nt"
FOLDERS = ["weather", "pollution", "sensor"]
REGION = "eu-west-1"
ENDPOINT = "https://rq5fbome43vbdgq7xoe7d6wbwa0ngkgr.lambda-url.eu-west-1.on.aws/"
CITY_NAME = "Belgrade"

boto3_client_singleton = Boto3ClientSingleton(region_name=REGION)


def list_files_in_s3(bucket, prefix):
    s3 = boto3_client_singleton.client('s3')
    paginator = s3.get_paginator("list_objects_v2")
    files = []
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for content in page.get("Contents", []):
            files.append(content["Key"])
    return files


def list_files_concurrently(bucket, folders):
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(list_files_in_s3, bucket, folder): folder for folder in folders}
        result = []
        for future in as_completed(futures):
            result.extend(future.result())
    return result


def download_s3_file(bucket, key):
    s3 = boto3_client_singleton.client('s3')
    file_obj = s3.get_object(Bucket=bucket, Key=key)
    file_content = file_obj["Body"].read().decode("utf-8")
    if not file_content.strip():  # Proveri da li je sadržaj prazan
        raise ValueError(f"File {key} is empty.")
    return file_content


def upload_s3_file(bucket, key, data):
    s3 = boto3_client_singleton.client('s3')
    s3.put_object(Bucket=bucket, Key=key, Body=data)


def fetch_city_estimates(date):
    headers = {"Authorization": f"Bearer {get_token()}"}
    params = {"date": date}
    try:
        response = requests.get(ENDPOINT, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        for city in data.get("info", []):
            if city["name"] == CITY_NAME:
                return city["estimated_no_people"]
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def get_token():
    secret_name = "tourist_estimate_token"
    client = boto3_client_singleton.client('secretsmanager')

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        print(f"Error retrieving secret: {e}")
        raise e

    return json.loads(get_secret_value_response['SecretString'])[secret_name]


def extract_date_from_key(folder, key):
    if folder == "sensor":
        match = re.search(r"time_nano=(\d+)", key)
        if match:
            timestamp = int(match.group(1))
            return pd.to_datetime(timestamp, unit='ns').strftime('%Y-%m-%d')
    else:
        match = re.search(r"time_date=(\d{4}-\d{2}-\d{2})", key)
        if match:
            return match.group(1)
    return None


def enrich_and_upload(bucket, folder, key):
    try:
        csv_content = download_s3_file(bucket, key)
        df = pd.read_csv(StringIO(csv_content))

        print(f"\nOriginal data from file {key}:\n")
        print(df.head())

        date = extract_date_from_key(folder, key)
        if not date:
            print(f"Skipping file {key}: unable to extract date.")
            return

        df["no_of_people_visited"] = fetch_city_estimates(date)

        print(f"\nEnriched data for file {key}:\n")
        print(df.head())

        enriched_csv = df.to_csv(index=False)
        upload_s3_file(bucket, key, enriched_csv)
        print(f"File enriched and overwritten: {key}")
    except ValueError as e:
        print(f"Skipping file {key} due to error: {e}")


def process_file(bucket, folder, file_key):
    print(f"Processing file: {file_key}")
    enrich_and_upload(bucket, folder, file_key)


def main():
    files = list_files_concurrently(BUCKET_NAME, FOLDERS)
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(process_file, BUCKET_NAME, file_key.split('/')[0], file_key) for file_key in files]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error processing file: {e}")


if __name__ == "__main__":
    main()
