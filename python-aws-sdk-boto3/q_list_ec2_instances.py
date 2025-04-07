import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from datetime import datetime, timezone

try:
    client = boto3.client('ec2')
    response = client.describe_instances()
    if not response['Reservations']:
        print("No EC2 Instances found")
    else:
        i=1
        b_date = datetime(2025, 1, 1, tzinfo=timezone.utc)
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_name = "UnNamed Instance"
                tags = instance.get('Tags', [])
                for tag in tags:
                    if tag['Key'] == 'Name':
                        instance_name = tag['Value']
                        break
                launch_time = instance.get('LaunchTime')
                if launch_time and launch_time < b_date:
                    print(f"Instance {i}: {instance_name}")
                    i += 1
except NoCredentialsError as e:
    print(f"No AWS Credentials found | {e}")
except PartialCredentialsError as e:
    print(f"Incomplete AWS Credentials | {e}")
except ClientError as e:
    print(f"AWS Client Error occured | {e}")
except Exception as e:
    print(f"Error: {e}")