import boto3

S3 = boto3.client('s3')
AWS_BUCKET_NAME = 'static.up.welt.de'
FOLDER_NAME = 'plus-catalogue'


def upload_data_to_s3_static(file_name):
    S3.upload_file(file_name, AWS_BUCKET_NAME, '%s/%s' % (FOLDER_NAME, file_name))


def retrieve_metadata_for_file(file):
    return S3.head_object(Bucket=AWS_BUCKET_NAME, Key='%s/%s' % (FOLDER_NAME, file))
