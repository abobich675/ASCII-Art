from dotenv import load_dotenv
import os
from minio import Minio
from io import BytesIO

load_dotenv()
client = Minio(os.getenv('MINIO_ENDPOINT', 'storage:9000'),
    access_key=os.getenv('MINIO_ROOT_USER'),
    secret_key=os.getenv('MINIO_ROOT_PASSWORD'),
    secure=False
)

def upload_blob_from_file(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""

    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # Upload the file, renaming it in the process
    client.fput_object(
        bucket_name, destination_blob_name, source_file_name,
    )
    print(
        source_file_name, "successfully uploaded as object",
        destination_blob_name, "to bucket", bucket_name,
    )

def upload_blob_from_bytes(bucket_name, image_bytes, destination_blob_name):
    """Uploads a file to the bucket."""
    
    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    data_stream = BytesIO(image_bytes)

    client.put_object(
        bucket_name,
        destination_blob_name,
        data_stream,
        length=len(image_bytes),
        content_type="image/png",
    )

    print(f"Uploaded image to {destination_blob_name}.")