import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def s3_client(region):
    return boto3.client('s3', region_name=region)

def bucket_exists(s3, bucket_name):
    try:
        response = s3.list_buckets()
        for bucket in response['Buckets']:
            if bucket['Name'] == bucket_name:
               return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def is_versioning_enabled(s3, bucket_name):
    if bucket_exists(s3, bucket_name):
        try:
            response = s3.get_bucket_versioning(Bucket=bucket_name)
            if response.get('Status') == 'Enabled':
                return True
            return False
        except Exception as e:
            print(f"Error: {e}")

def create_bucket(s3, bucket_name, region):
    if not bucket_exists(s3, bucket_name):
        try:
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
            print(f"Bucket {bucket_name} created successfully in {region}")       
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"The Bucket {bucket_name} is already present. Hence the operation is skipped.")

def enable_versioning(s3, bucket_name):
    if not is_versioning_enabled(s3, bucket_name):
        try:
            s3.put_bucket_versioning(Bucket=bucket_name, VersioningConfiguration={'MFADelete': 'Disabled', 'Status': 'Enabled'})
            print(f"Versioning is enabled for the {bucket_name} Bucket")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Versioning was already enabled for the bucket '{bucket_name}'.")
try:
    bucket_name = input("Enter the Bucket Name to Create: ").strip()
    region = input("Enter the region in which you want to create the bucket: ").strip()
    s3 = s3_client(region)
    create_bucket(s3, bucket_name, region)
    enable_versioning(s3, bucket_name)

except NoCredentialsError as e:
    print(f"No AWS Credentials found | {e}")
except PartialCredentialsError as e:
    print(f"Incomplete AWS Credentials | {e}")
except ClientError as e:
    print(f"AWS Client Error occured | {e}")
except Exception as e:
    print(f"Error: {e}")