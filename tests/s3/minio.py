import boto3

LOCAL_S3_PROXY_SERVICE_URL = "http://localhost:9000"

s3 = boto3.client(
    "s3",
    aws_access_key_id="minio",
    aws_secret_access_key="minio_pwd123",
    endpoint_url=LOCAL_S3_PROXY_SERVICE_URL,
)

print(s3.list_buckets())

response = s3.list_objects_v2(Bucket="bde-warehouse")

if "Contents" in response:
    for obj in response["Contents"]:
        print(obj["Key"])
else:
    print("Bucket is empty")
