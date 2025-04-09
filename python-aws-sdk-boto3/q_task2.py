import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def s3_client(region):
    return boto3.client('s3', region_name=region)

def upload_to_s3(s3, bucket_name, file_path, s3_key):
    tag = None
    try:
        with open(file_path, 'rb') as file_data: 
            if file_path.endswith('.csv'):
                tag = 'type=dataset'
                s3.put_object(Bucket=bucket_name, Key=s3_key, Body=file_data, Tagging=tag)
            elif file_path.endswith('.json'):
                tag = 'type=config'
                s3.put_object(Bucket=bucket_name, Key=s3_key, Body=file_data, Tagging=tag)
            elif file_path.endswith('.zip'):
                tag = 'type=compressed'
                s3.put_object(Bucket=bucket_name, Key=s3_key, Body=file_data, Tagging=tag)
            else:
                s3.put_object(Bucket=bucket_name, Body=file_data, Key=s3_key)
        return tag
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"Error uploading file: {e}")
        
try: 
    region = input("Enter the region: ").strip()
    s3 = s3_client(region)
    bucket_name = input("Enter the Bucket Name: ").strip()
    file_path = input("Enter the File Name ( Ex: test.txt ): ").strip()
    s3_key = input("Enter the Key (Ex: uploads/test.txt ): ").strip()
    tag = upload_to_s3(s3, bucket_name, file_path, s3_key)

    if tag:
        print(f"File '{file_path}' uploaded with tag {tag}")
    else:
        print(f"File '{file_path}' uploaded without any tag")


except NoCredentialsError as e:
    print(f"No AWS Credentials found | {e}")
except PartialCredentialsError as e:
    print(f"Incomplete AWS Credentials | {e}")
except ClientError as e:
    print(f"AWS Client Error occured | {e}")
except Exception as e:
    print(f"Error: {e}")