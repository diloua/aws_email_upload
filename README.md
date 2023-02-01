# # Epilot AWS assignement

Simple file service on AWS that allows a user to securely store files and be notified by email when the file is accessed

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Installing

```
git clone https://github.com/aws_email_upload
cd aws_email_upload
pip install -r requirements.txt
```

### Running
```
python app.py
```


## Code description

### verify_email

The verify_email function takes in an email address as an argument and calls the lambda function that verifies whether the email address is valid or not.

### upload_file

The upload_file function takes in a file as argument and calls the lambda function that uploads the file on AWS.

### app.py

The main function running the app

## Lambda functions:
```
cd util/lambda_functions
```

### uploadNotifyFile:
Decodes the incoming binary file data from the request body into a byte string.
Reads the bucket name, file key, and email address from the request.
Verifies that the email address is a verified email address on Amazon Simple Email Service (SES).
Checks if the file already exists in the S3 bucket and returns an error if it does.
Uploads the file to the S3 bucket if it does not exist.
Checks if the file was uploaded successfully to the S3 bucket.
Sends an email notification to the provided email address indicating that a file was uploaded to the S3 bucket. The email includes the bucket name, file key, and the time the file was uploaded.

### verifyAddress:
Connects to the Amazon SES (Simple Email Service) service.
Gets the email address to add to verified emails.
Checks if the email has been verified using ses.list_verified_email_addresses().
If the email is already verified, returns a response with status code 200, the email, and a message "Email is already verified".
If the email has not been verified, it tries to add the email to verified emails using ses.verify_email_identity(EmailAddress=email).
If successful, it prints "Email added to verified emails" and returns the result.

## Running the tests

Very simple API tests for each of the functions can be found in the tests directory. To run the tests, simply run the following command:
```
python -m unittest discover
```

## Author

Oualid El Bouanani
