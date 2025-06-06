import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

s3 = boto3.client('s3')

def upload_to_s3(bucket_name, file_path, s3_key):
    with open(file_path,'rb') as file_data:
        return s3.put_object(Body=file_data, Bucket=bucket_name, Key=s3_key)
    
try:
    bucket_name = input("Enter the Bucket Name: ").strip()
    file_path = input("Enter the File Name ( Ex: test.txt ): ").strip()
    s3_key = input("Enter the Key (Ex: uploads/test.txt ): ").strip()
    upload_to_s3(bucket_name, file_path, s3_key)
    print(f"File {file_path} uploaded successfully to s3://{bucket_name} Bucket")

except NoCredentialsError as e:
    print(f"No AWS Credentials found | {e}")
except PartialCredentialsError as e:
    print(f"Incomplete AWS Credentials | {e}")
except ClientError as e:
    print(f"AWS Client Error occured | {e}")
except Exception as e:
    print(f"Error: {e}")