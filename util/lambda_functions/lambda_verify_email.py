import boto3

def lambda_handler(event, context):
    """
    Lambda function to verify email address of user
    """
    # Get the email address to add to verified emails
    email = event["email"]
    
    # Connect to the Amazon SES service
    ses = boto3.client("ses")
    #Check if the email has been verified
    response = ses.list_verified_email_addresses()
    if email in response['VerifiedEmailAddresses']:
        return {
            "statusCode": 200,
            "email": email,
            "message": "Email is already verified"
        }
    # Try to add the email to verified emails
    try:
        result = ses.verify_email_identity(EmailAddress=email)
        print("Email added to verified emails:", email)
        return result
    except ses.exceptions.MessageRejected as e:
            print("Error adding email to verified emails:", email, e)
            raise e
