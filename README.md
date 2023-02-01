# # Project Title

A brief description of your project and its purpose.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Installing

A step by step series of examples that tell you how to get a development env running.
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

## Running the tests

Tests for each of the functions can be found in the tests directory. To run the tests, simply run the following command:
```
python -m unittest discover
```

## Author

Oualid El Bouanani
