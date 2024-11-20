import sys
import requests
import boto3
from botocore.exceptions import ClientError
import json
from datetime import datetime

ENDPOINT = "https://rq5fbome43vbdgq7xoe7d6wbwa0ngkgr.lambda-url.eu-west-1.on.aws/"
REGION = "eu-west-1"

def get_secret():
    secret_name = "tourist_estimate_token"
    region_name = "eu-west-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
        aws_access_key_id=sys.argv[1],
        aws_secret_access_key=sys.argv[2],
        aws_session_token=sys.argv[3]
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        print(f"Error retrieving secret: {e}")
        raise e

    return json.loads(get_secret_value_response['SecretString'])[secret_name]

def fetch_city_estimates(date, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "date": date
    }
    try:
        response = requests.get(ENDPOINT, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_estimates(data):
    if data and 'info' in data:
        print(f"Tourist estimates for {data['for_date']}:")
        for city_estimate in data['info']:
            city_name = city_estimate['name']
            estimated_no_people = city_estimate['estimated_no_people']
            print(f"{city_name}: {estimated_no_people} people")
    else:
        print("No data available or invalid response format.")

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def main():
    try:
        token = get_secret()
    except Exception as e:
        print(f"Failed to retrieve token: {e}")
        sys.exit(1)

    date = input("Enter the date (YYYY-MM-DD): ")

    while not is_valid_date(date):
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
        date = input("Enter the date (YYYY-MM-DD): ")

    data = fetch_city_estimates(date, token)
    display_estimates(data)

if __name__ == "__main__":
    main()
