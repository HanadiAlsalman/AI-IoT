import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_bucket_objects(hanadi):
    """List objects in an S3 bucket"""
    s3 = boto3.client('s3', region_name='eu-north-1')
    try:
        response = s3.list_objects_v2(Bucket=hanadi)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f' - {obj["Key"]}')
        else:
            print(f'Bucket {hanadi} is empty.')
    except NoCredentialsError:
        print('Credentials not available.')
    except PartialCredentialsError:
        print('Incomplete credentials provided.')

if __name__ == '__main__':
    hanadi = 'your-existing-bucket-name'  # Ändra till din bucket
    list_bucket_objects("hanadi")

