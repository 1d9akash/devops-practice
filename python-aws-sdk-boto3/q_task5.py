from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from q_task1 import s3_client, bucket_exists
import requests
import json
def generate_presigned_url(s3, bucket_name, object_name):
    if bucket_exists(s3, bucket_name):
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
                 f"arn:aws:s3:::{bucket_name}/*"
               ],
               "Condition": {
                   "IpAddress": {
                       "aws:SourceIp": ip_range
                   }
               },
               "Principal": "*"
             }
           ]
         }
        try:
            s3.put_bucket_policy(Bucket=bucket_name,Policy=json.dumps(policy))
            result = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name,'Key': object_name}, ExpiresIn=360)
            print(f"Pre-Signed URL generated (Valid for 5 mins): {result}")
        except ClientError as e:
            print(f"AWS Client Error occured | {e}")

if __name__ == "__main__":
    try:
        my_ip = requests.get("https://api.ipify.org").text.strip()
        print(f"My public IP is: {my_ip}")
        ip_range = my_ip + "/29"
        region = input("Enter the region: ").strip()
        bucket_name = input("Enter the Bucket Name: ").strip()
        object_name = input("Enter the Key (Ex: uploads/test.txt ): ").strip()
        s3 = s3_client(region)
        generate_presigned_url(s3, bucket_name, object_name)
    except NoCredentialsError as e:
        print(f"No AWS Credentials found | {e}")
    except PartialCredentialsError as e:
        print(f"Incomplete AWS Credentials | {e}")
    except ClientError as e:
        print(f"AWS Client Error occured | {e}")
    except Exception as e:
        print(f"Error: {e}")