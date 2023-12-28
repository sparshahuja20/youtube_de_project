import os
from resources.dev import config
from src.main.utility.s3_client_object import *
from src.main.utility.encrypt_decrypt import *
s3_client_provider = S3ClientProvider(config.aws_access_key, config.aws_secret_key)
s3_client = s3_client_provider.get_client()

local_file_path = "/Users/ayushisachdev/Documents/ofc_ss/projects/spark_projects/raw_data/"
def upload_to_s3(s3_directory, s3_bucket, local_file_path):
    s3_prefix = f"{s3_directory}"
    try:
        for root, dirs, files in os.walk(local_file_path):
            for file in files:
                print(file)
                local_file_path = os.path.join(root, file)
                s3_key = f"{s3_prefix}{file}"
                s3_client.upload_file(local_file_path, s3_bucket, s3_key)
    except Exception as e:
        raise e

s3_directory = "sales_data/"
s3_bucket = config.bucket_name
upload_to_s3(s3_directory, s3_bucket, local_file_path)