import boto3
from pprint import pprint
client = boto3.client('ec2')
response = client.describe_instances()
# with open("output.txt", "w") as f:
#     print(response,file=f)
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"{instance['InstanceId']} - {instance['PrivateIpAddress']} - {instance['InstanceType']}")
        for name in reservation['Tags']:
            print(f"{name['Name']}")