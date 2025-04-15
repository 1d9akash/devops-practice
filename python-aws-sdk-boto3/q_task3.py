from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from q_task1 import s3_client, bucket_exists

def s3_lifecycle_mgmt(s3, bucket_name):
    if bucket_exists(s3, bucket_name):
        lifecycle_config = {
            'Rules':
            [
                {
                    'ID': 'Transition to Glacier After 7 Days',
                    'Filter': {'Prefix': ''},
                    'Status': 'Enabled',
                    'Transitions': [{'Days': 7, 'StorageClass': 'GLACIER'}]
                },
                
#                {
#                    'ID': 'Protect Objects older than 90 Days with Tag type=config',
#                    'Filter': {'And':{'Prefix': '', 'Tags': [{'Key': 'type', 'Value': 'config'}]}},
#                    'Status': 'Enabled'
#                    'Expiration': {'Days': 90}
#                },
                
#                {
#                    'ID': 'Delete Objects older than 90 Days',
#                    'Filter': {'Prefix': ''},
#                    'Status': 'Enabled',
#                    'Expiration': {'Days': 90}
#                },

#                {
#                    'ID': 'Enable Intelligent-Tiering For files with tag type=config',
#                    'Filter': {'And':{'Prefix': '', 'Tags': [{'Key': 'type', 'Value': 'config'}]}},
#                    'Status': 'Enabled',
#                    'Transitions': [{'Days':0, 'StorageClass': 'INTELLIGENT_TIERING'}]
#                }
            ]
        }
        try:
            s3.put_bucket_lifecycle_configuration(Bucket=bucket_name,LifecycleConfiguration=lifecycle_config)
            print("Lifecycle rule applied: Move to Glacier after 7 days, delete objects after 90 days except objects tagged with type=config and Enabled Intelligent-Tiering For files size greater than 100MB")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Bucket {bucket_name} Not found")

if __name__ == "__main__":
    try:
        region = input("Enter the region: ").strip()
        bucket_name = input("Enter the Bucket Name: ").strip()
        s3 = s3_client(region)
        s3_lifecycle_mgmt(s3,bucket_name)

    except NoCredentialsError as e:
        print(f"No AWS Credentials found | {e}")
    except PartialCredentialsError as e:
        print(f"Incomplete AWS Credentials | {e}")
    except ClientError as e:
        print(f"AWS Client Error occured | {e}")
    except Exception as e:
        print(f"Error: {e}")