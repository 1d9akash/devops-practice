import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

s3 = boto3.client('s3')

def upload_to_s3(bucket_name, file_path, s3_key):
    return s3.upload_file(file_path, bucket_name, s3_key)
# def list_s3_objects(bucket_name):
#     return s3.list_objects_v2(Bucket=bucket_name)
try:
    bucket_name = input("Enter the Bucket Name: ").strip()
    file_path = input("Enter the File Name ( Ex: test.txt ): ").strip()
    s3_key = input("Enter the Key (Ex: uploads/test.txt ): ").strip()
    upload_to_s3(bucket_name, file_path, s3_key)
    print(f"File {file_path} uploaded successfully to s3://{bucket_name} Bucket")
#    result = s3.list_objects_v2(Bucket=bucket_name)
#    with open("sample-s3-listobjects.txt", "w") as f:
#        print(result,file=f)
except NoCredentialsError as e:
    print(f"No AWS Credentials found | {e}")
except PartialCredentialsError as e:
    print(f"Incomplete AWS Credentials | {e}")
except ClientError as e:
    print(f"AWS Client Error occured | {e}")
except Exception as e:
    print(f"Error: {e}")