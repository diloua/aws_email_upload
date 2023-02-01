import boto3
import json
import base64

s3 = boto3.client("s3")
ses = boto3.client("ses")

def lambda_handler(event, context):
    """
    Lambda function to upload file to the s3 bucket
    """
    file = base64.b64decode(event['body'].encode("utf-8"))
    bucket = event['bucket']
    key = event['key']
    email = event['email']

    # Check if the email is verified
    verified_emails = ses.list_verified_email_addresses()['VerifiedEmailAddresses']
    if email not in verified_emails:
        return {
            "statusCode": 400,
            "message": json.dumps("Email address is not verified")
        }

    # Check if file already exists
    try:
        s3.head_object(Bucket=bucket, Key=key)
        return {
            "statusCode": 400,
            "message": json.dumps("File already exists and cannot be overwritten")
        }
    except:
        # Upload the file to the S3 bucket
        try:
            s3.put_object(Bucket=bucket, Key=key, Body=file)
        except Exception as e:
            return {
                'statusCode': 500,
                'message': json.dumps(f'File upload to S3 bucket failed: {e}')
            }

    # Check if file was uploaded successfully
    try:
        s3.head_object(Bucket=bucket, Key=key)
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "message": json.dumps("File not found")
        }

    # Send email notification
    email_body = f"A file has been uploaded to the following S3 bucket: {bucket} with the key: {key}"
    ses.send_email(
        Destination={
            'ToAddresses': [email]
        },
        Message={
            'Body': {
                'Text': {
                    'Data': email_body
                }
            },
            'Subject': {
                'Data': "File Upload Notification"
            }
        },
        Source="no.reply.epilot.test@gmail.com"
    )

    return {
        "statusCode": 200,
        "message": json.dumps("File uploaded and email sent successfully")
    }

