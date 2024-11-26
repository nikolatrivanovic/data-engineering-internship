import boto3
import sys
import pandas as pd
from io import StringIO


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

boto3_client_singleton = Boto3ClientSingleton(region_name='eu-west-1')


def list_first_file_in_s3_folder(bucket, folder):
    s3 = boto3_client_singleton.client('s3')
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket, Prefix=folder):
        for content in page.get("Contents", []):
            if not content["Key"].endswith('/'):
                return content["Key"]
    return None


def download_s3_file(bucket, key):
    s3 = boto3_client_singleton.client('s3')
    file_obj = s3.get_object(Bucket=bucket, Key=key)
    file_content = file_obj["Body"].read().decode("utf-8")
    return file_content


def extract_column_names(bucket, folders):
    column_names = {}
    for folder in folders:
        first_file = list_first_file_in_s3_folder(bucket, folder)
        if first_file:
            csv_content = download_s3_file(bucket, first_file)
            df = pd.read_csv(StringIO(csv_content))
            column_names[folder] = df.columns.tolist()
    return column_names


def generate_sql_scripts(column_names):
    sql_scripts = {}
    for folder, columns in column_names.items():
        column_definitions = ',\n  '.join([f"{col} STRING" for col in columns])
        sql_script = f"""
        CREATE EXTERNAL TABLE IF NOT EXISTS my_db_nt_levi9.{folder} (
          {column_definitions}
        )
            ROW FORMAT SERDE
              'org.apache.hadoop.hive.serde2.OpenCSVSerde'
            WITH SERDEPROPERTIES (
              'escapeChar'='\\\\',
              'quoteChar'='\\"',
              'separatorChar'=',')
            STORED AS INPUTFORMAT
              'org.apache.hadoop.mapred.TextInputFormat'
            OUTPUTFORMAT
              'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
            LOCATION
              's3://processed-data-levi9-nt/{folder}'
            TBLPROPERTIES (
              'has_encrypted_data'='false',
              'skip.header.line.count'='1');
        """
        sql_scripts[folder] = sql_script.strip()
    return sql_scripts


def main():
    column_names = extract_column_names(BUCKET_NAME, FOLDERS)
    sql_scripts = generate_sql_scripts(column_names)
    for folder, sql_script in sql_scripts.items():
        with open(f"create_table_{folder}.sql", "w") as file:
            file.write(sql_script)
        print(f"SQL script for {folder} generated and saved to create_table_{folder}.sql")


if __name__ == "__main__":
    main()
