import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

s3 = boto3.client('s3')
def bucket_exists(bucket_name):
    response = s3.list_buckets()
    for buckets in response['Buckets']:
        if buckets['Name'] == bucket_name:
#           print(f"The Bucket {bucket_name} is already present. Hence the operation is skipped.")
           return True
    return False
def create_bucket(bucket_name,region):
    if not bucket_exists(bucket_name):
        try:
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
            print(f"Bucket {bucket_name} created successfully in {region}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"The Bucket {bucket_name} is already present. Hence the operation is skipped.")
    
try:
    bucket_name = input("Enter the Bucket Name to Create: ").strip()
    region = input("Enter the region in which you want to create the bucket: ").strip()

#    bucket_exists(bucket_name)
    create_bucket(bucket_name,region)

except NoCredentialsError as e:
    print(f"No AWS Credentials found | {e}")
except PartialCredentialsError as e:
    print(f"Incomplete AWS Credentials | {e}")
except ClientError as e:
    print(f"AWS Client Error occured | {e}")
except Exception as e:
    print(f"Error: {e}")