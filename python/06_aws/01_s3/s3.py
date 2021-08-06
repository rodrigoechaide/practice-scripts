# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/examples.html

import boto3
from botocore.exceptions import ClientError
import logging
import os

def list_buckets(session):
    # Let's use Amazon S3 resource method
    s3 = session.resource('s3')

    # Print out bucket names
    for bucket in s3.buckets.all():
        print(bucket.name)

def upload_file(session, file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3 = session.client('s3')
    try:
        response = s3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_fileobj(session, file_name, bucket, object_name=None, ExtraArgs=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
    s3 = session.client('s3')
    with open(file_name, "rb") as f:
        if ExtraArgs is None:
            s3.upload_fileobj(f, bucket, object_name)
        else:
            s3.upload_fileobj(f, bucket, object_name, ExtraArgs)
    return True

def delete_object(method, session, object_name, bucket):
    if method == "resource":
        s3 = session.resource('s3')
        s3.Object(bucket, object_name).delete()
    if method == "client":
        s3 = session.client('s3')
        try:
            response = s3.delete_object(Key=object_name, Bucket=bucket)
        except ClientError as e:
            logging.error(e)
            return False
    return True

def download_object(method, session, bucket, path, key):
    if method == "resource":
        s3 = session.resource("s3")
        s3.meta.client.download_file(bucket, path + '/' + key, './' + key)
    if method == "client":
        s3 = session.client("s3")
        s3.download_file(bucket, path + '/' + key, key)
    return True

def delete_folder(session, bucket, prefix):
    """Delete all objects with the same path prefix

    :param session: Session object
    :param bucket: Bucket name
    :param prefix: Prefix to delete objects under
    """
    s3 = session.resource("s3")
    bucket = s3.Bucket(bucket)
    bucket.objects.filter(Prefix=prefix).delete()

def list_files(session, bucket, prefix):
    s3 = session.client("s3")
    """List files in specific S3 URL"""
    response = s3.list_objects(Bucket=bucket, Prefix=prefix)
    for content in response.get('Contents', []):
        yield content.get('Key')


### Main Program ###
AWS_REGION = os.environ.get('AWS_REGION',"us-east-1")

try:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )
except:
    session = boto3.Session(region_name=AWS_REGION)


# Upload an Object
# response = upload_file(session, "dummy.txt", "qa-tradersync", "dummy/dummy.txt")
# response = upload_fileobj(session, "dummy2.txt", "qa-tradersync", "dummy/dummy2.txt")
# response = upload_fileobj(session, "picture.png", "qa-tradersync", "picture.png", {"ACL": "public-read", "ContentType": "image/png"})

# Delete an Object
# response = delete_object("client", session, "dummy.txt", "qa-tradersync")
# response = delete_object("resource", session, "picture.png", "qa-tradersync")

# Download an Object
# response = download_object("client", session, "qa-tradersync", "user_backups", "backup_adminuser_2021-08-02_17_31_23_1.csv")

# Delete a Folder
response = delete_folder(session, "qa-tradersync", "dummy")

# List files
file_list = list_files(session, "qa-tradersync", "dummy")
for file in file_list:
    print(f'File found: {file}')