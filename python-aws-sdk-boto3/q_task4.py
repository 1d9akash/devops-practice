import json
import requests
from q_task1 import s3_client, bucket_exists
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def block_all_public_access(s3, bucket_name):
    if bucket_exists(s3, bucket_name):
        try:
            s3.put_public_access_block(Bucket=bucket_name, PublicAccessBlockConfiguration={'BlockPublicAcls': True,'IgnorePublicAcls': True,'BlockPublicPolicy': True,'RestrictPublicBuckets': True})
            print("Public access blocked, ", end="")
        except ClientError as e:
            print(f"AWS Client Error occured | {e}")
    else:
        print(f"Bucket {bucket_name} doesnot exists")

def allow_access(s3, bucket_name):
    policy = {
               "Id": "Policy1744391477426",
               "Version": "2012-10-17",
               "Statement": [
                 {
                   "Sid": "Stmt1744391475954",
                   "Action": [
                     "s3:GetObject"
                   ],
                   "Effect": "Allow",
                   "Resource": [
                     f"arn:aws:s3:::{bucket_name}",
                     f"arn:aws:s3:::{bucket_name}/*"
                   ],
                   "Condition": {
                       "IpAddress": {
                           "aws:SourceIp": my_ip + "/29"
                       }
                   },
                   "Principal": {
                     "AWS": [
                       "arn:aws:iam::121414159343:role/S3DataProcessor"
                     ]
                   }
                 }
               ]
             }
    try:
        s3.put_bucket_policy(Bucket=bucket_name,Policy=json.dumps(policy))
        print(f"Allowed access only from S3DataProcessor and Restricted downloads to {my_ip}/29 range")
    except ClientError as e:
        print(f"AWS Client Error occured | {e}")

if __name__ == "__main__":
    try:
        my_ip = requests.get("https://api.ipify.org").text
        region = input("Enter the region: ").strip()
        bucket_name = input("Enter the Bucket Name: ").strip()
        s3 = s3_client(region)
        block_all_public_access(s3, bucket_name)
        allow_access(s3, bucket_name)
    except NoCredentialsError as e:
        print(f"No AWS Credentials found | {e}")
    except PartialCredentialsError as e:
        print(f"Incomplete AWS Credentials | {e}")
    except ClientError as e:
        print(f"AWS Client Error occured | {e}")
    except Exception as e:
        print(f"Error: {e}")