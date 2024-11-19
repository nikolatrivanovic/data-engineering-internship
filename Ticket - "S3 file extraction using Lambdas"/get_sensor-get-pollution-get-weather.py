import boto3
import os
import time
from concurrent.futures import ThreadPoolExecutor

def copy_object(s3_client, source_bucket, destination_bucket, source_key, destination_key):
    try:
        s3_client.copy_object(
            CopySource={'Bucket': source_bucket, 'Key': source_key},
            Bucket=destination_bucket,
            Key=destination_key
        )
    except Exception as e:
        print(e)


def lambda_handler(event, context):
    s3_client = boto3.client('s3', region_name='eu-north-1')
    source_bucket = "nine-air-weather-data"
    destination_bucket = "bucket-14-11-nt-v2"
    folder_prefix = os.environ['FOLDER_PREFIX']

    try:
        paginator = s3_client.get_paginator('list_objects_v2')
        page_iterator = paginator.paginate(Bucket=source_bucket, Prefix=folder_prefix)

        with ThreadPoolExecutor(max_workers=10) as executor:
            for page in page_iterator:
                if 'Contents' in page:
                    for obj in page['Contents']:
                        source_key = obj['Key']
                        if 'Beograd' in source_key:
                            destination_key = source_key
                            executor.submit(copy_object, s3_client, source_bucket, destination_bucket, source_key, destination_key)

    except Exception as e:
        print(f"Error: {str(e)}")
        raise e
