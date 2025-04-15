from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from q_task1 import s3_client, bucket_exists

def calc_bucket_size(s3, bucket_name):
    if bucket_exists(s3, bucket_name):
        try:
            paginator = s3.get_paginator('list_objects_v2')
            response_iterator = paginator.paginate(Bucket=bucket_name)
            total_size = 0
            for page in response_iterator:
                if 'Contents' in page:
                    for obj in page['Contents']:
                        total_size += obj.get('Size', 0)
            print(f"{total_size/(1024**3):.2f} GB")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Bucket {bucket_name} Not found")   

if __name__  == "__main__":
    try:
        region = input("Enter the region: ").strip()
        bucket_name = input("Enter the Bucket Name: ").strip()
        s3 = s3_client(region)
        calc_bucket_size(s3, bucket_name)

    except NoCredentialsError as e:
        print(f"No AWS Credentials found | {e}")
    except PartialCredentialsError as e:
        print(f"Incomplete AWS Credentials | {e}")
    except ClientError as e:
        print(f"AWS Client Error occured | {e}")
    except Exception as e:
        print(f"Error: {e}")
