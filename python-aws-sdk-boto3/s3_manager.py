from q_task1 import s3_client, create_bucket, enable_versioning
from q_task2 import upload_to_s3
from q_task3 import s3_lifecycle_mgmt
from q_task4 import block_all_public_access, allow_access
from q_task5 import generate_presigned_url
from q_task6 import calc_bucket_size_largest_files_cost_est
import requests
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def menu():
    print("\n========")
    print("AWS S3 Management Tool - Choose an action:")
    print("1. Create & Configure Buckets")
    print("2. Upload & Tag Files")
    print("3. Automate Data Lifecycle Management")
    print("4. Apply Security Policies")
    print("5. Generate Pre-Signed URLs")
    print("6. Monitor & Optimize Storage")
    print("7. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-7): ").strip()

    try:
        if choice == '1':
            bucket_name = input("Enter the Bucket Name to Create: ").strip()
            region = input("Enter the region: ").strip()
            s3 = s3_client(region)
            create_bucket(s3, bucket_name, region)
            enable_versioning(s3, bucket_name)

        elif choice == '2':
            region = input("Enter the region: ").strip()
            s3 = s3_client(region)
            bucket_name = input("Enter the Bucket Name: ").strip()
            file_path = input("Enter the File Name (Ex: test.txt): ").strip()
            s3_key = input("Enter the Key (Ex: uploads/test.txt): ").strip()
            tag = upload_to_s3(s3, bucket_name, file_path, s3_key)
            if tag:
                print(f"File '{file_path}' uploaded with tag {tag}")
            else:
                print(f"File '{file_path}' uploaded without any tag")

        elif choice == '3':
            region = input("Enter the region: ").strip()
            bucket_name = input("Enter the Bucket Name: ").strip()
            s3 = s3_client(region)
            s3_lifecycle_mgmt(s3, bucket_name)

        elif choice == '4':
            my_ip = requests.get("https://api.ipify.org").text.strip()
            region = input("Enter the region: ").strip()
            bucket_name = input("Enter the Bucket Name: ").strip()
            s3 = s3_client(region)
            block_all_public_access(s3, bucket_name)
            allow_access(s3, bucket_name)

        elif choice == '5':
            my_ip = requests.get("https://api.ipify.org").text.strip()
            ip_range = my_ip + "/29"
            region = input("Enter the region: ").strip()
            bucket_name = input("Enter the Bucket Name: ").strip()
            object_name = input("Enter the Key (Ex: uploads/test.txt): ").strip()
            s3 = s3_client(region)
            generate_presigned_url(s3, bucket_name, object_name, ip_range)

        elif choice == '6':
            region = input("Enter the region: ").strip()
            bucket_name = input("Enter the Bucket Name: ").strip()
            s3 = s3_client(region)
            calc_bucket_size_largest_files_cost_est(s3, bucket_name)

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose between 1 and 7.")

    except NoCredentialsError as e:
        print(f"No AWS Credentials found | {e}")
    except PartialCredentialsError as e:
        print(f"Incomplete AWS Credentials | {e}")
    except ClientError as e:
        print(f"AWS Client Error occurred | {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")