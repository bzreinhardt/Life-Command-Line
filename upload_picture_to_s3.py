import os
import sys

S3_BUCKET                 = "zaaron-personal"
S3_KEY                    = os.environ.get("AWSAccessKeyId")
S3_SECRET                 = os.environ.get("AWSSecretKey")
S3_LOCATION               = 'https://s3-us-west-1.amazonaws.com/{}'.format(S3_BUCKET)

SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000

import boto3, botocore


def upload_file_to_s3(file, bucket_name, acl="public-read"):
    try:
        s3.upload_file(
            file,
            bucket_name,
            os.path.basename(file),
            ExtraArgs={'ACL': 'public-read',
                       'ContentType':'image'}
        )

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e

    return "{}/{}".format(S3_LOCATION,  os.path.basename(file).replace(" ", "+"))


if __name__== '__main__':
    s3 = boto3.client(
       "s3",
       aws_access_key_id=S3_KEY,
       aws_secret_access_key=S3_SECRET
    )
    for file in sys.argv[1:]:
        full_file = os.path.abspath(file)
        url = upload_file_to_s3(full_file, S3_BUCKET)
        print(url)
