from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from q_task1 import s3_client, bucket_exists

def calc_bucket_size_largest_files_cost_est(s3, bucket_name):
    if bucket_exists(s3, bucket_name):
        try:
            paginator = s3.get_paginator('list_objects_v2')
            response_iterator = paginator.paginate(Bucket=bucket_name)
            total_size = 0
            files = []
            for page in response_iterator:
                if 'Contents' in page:
                    for obj in page['Contents']:
                        key = obj.get('Key')
                        size = obj.get('Size')
                        files.append((key,size))
                        total_size += obj.get('Size', 0)
            files_sorted = sorted(files, key=lambda x: x[1], reverse=True)
            result = total_size/(1024**3)
            print(f"Total Storage Used: {result:.2f} GB")
            print("Largest Files: ", end="")
            for key, size in files_sorted[:5]:
                print(f"{key} ({size/(1024**2):.2f} MB), ",end="")
            print(f"\nEstimated Monthly Cost: ${(result*0.025):.2f} USD")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Bucket {bucket_name} Not found")   

if __name__  == "__main__":
    try:
        region = input("Enter the region: ").strip()
        bucket_name = input("Enter the Bucket Name: ").strip()
        s3 = s3_client(region)
        calc_bucket_size_largest_files_cost_est(s3, bucket_name)

    except NoCredentialsError as e:
        print(f"No AWS Credentials found | {e}")
    except PartialCredentialsError as e:
        print(f"Incomplete AWS Credentials | {e}")
    except ClientError as e:
        print(f"AWS Client Error occured | {e}")
    except Exception as e:
        print(f"Error: {e}")
