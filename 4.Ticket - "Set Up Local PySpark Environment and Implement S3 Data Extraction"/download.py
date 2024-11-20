import boto3
import sys
import os

def download():
    s3_client = boto3.client(
        's3',
        aws_access_key_id=sys.argv[1],
        aws_secret_access_key=sys.argv[2],
        aws_session_token=sys.argv[3],
        region_name='us-west-2'
    )
    bucket_name = 'bucket-14-11-nt-v2'
    prefix = 'weather/1297 - Dorćol 2, Beograd, Serbia/'
    paginator = s3_client.get_paginator('list_objects_v2')
    local_directory = os.path.join(os.getcwd(), 'downloaded_files')

    if not os.path.exists(local_directory):
        os.makedirs(local_directory)

    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
        for obj in page.get('Contents', []):
            file_key = obj['Key']
            if file_key:
                local_file_path = os.path.join(local_directory, file_key.split('/')[-1])
                s3_client.download_file(bucket_name, file_key, local_file_path)
                print(f"Downloaded: {file_key}")
