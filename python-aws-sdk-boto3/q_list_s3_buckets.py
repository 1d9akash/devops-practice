import boto3
client = boto3.client('s3')
response = client.list_buckets()
i = 1
for bucket in response['Buckets']:
    print(f"- Bucket {i}: {bucket['Name']}")
    i += 1