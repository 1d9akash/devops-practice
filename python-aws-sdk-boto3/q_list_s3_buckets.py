import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

try:
    client = boto3.client('s3')
    response = client.list_buckets()
    i = 1
    for bucket in response['Buckets']:
        print(f"- Bucket {i}: {bucket['Name']}")
        i += 1
except NoCredentialsError as e:
    print(f"No AWS Credentials found | {e}")
except PartialCredentialsError as e:
    print(f"Incomplete AWS Credentials | {e}")
except ClientError as e:
    print(f"AWS Client Error occured | {e}")
except Exception as e:
    print(f"Error: {e}")