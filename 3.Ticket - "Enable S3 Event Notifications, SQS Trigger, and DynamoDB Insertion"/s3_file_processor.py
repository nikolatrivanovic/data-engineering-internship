import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['DYNAMODB_TABLE_NAME']
table = dynamodb.Table(table_name)

ALLOWED_FOLDERS = ['pollution/', 'sensor/', 'weather/']


def lambda_handler(event, context):
    try:
        for record in event['Records']:
            message_body = json.loads(record['body'])
            s3_event_records = message_body.get("Records", [])

            for s3_record in s3_event_records:
                bucket_name = s3_record['s3']['bucket']['name']
                object_key = s3_record['s3']['object']['key']

                if not any(object_key.startswith(folder) for folder in ALLOWED_FOLDERS):
                    raise Exception("File not put into correct folder. Try again")

                file_name = object_key.split('/')[-1]
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                status = 0

                response = table.put_item(
                    Item={
                        'file_name': file_name,
                        'timestamp': timestamp,
                        'status': status
                    }
                )
    except Exception as e:
        print(f"Error processing record: {record}. Error: {str(e)}")
