import requests
import base64
import config
import upload_file
import verify_email
import unittest

while True:
    user_email = input("Please enter your email: ")
    if not verify_email.verifyEmail(user_email):
        continue
    else:
        break

# Ensure that the file exists
while True:
    file_name = input("Please enter the path of the file you want to upload to the bucket: ")
    try:
        with open(file_name, "rb"):
            break
    except FileNotFoundError:
        print("The file could not be found. Please enter a valid file path.")

if upload_file.uploadFile(file_name, user_email):
    print("You have successfully uploaded your file!")
else:
    print("An error occurred while uploading your file.")

