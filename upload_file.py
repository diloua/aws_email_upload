import requests
import base64
import config

def uploadFile(file_name: str, email: str) -> bool:
    """
    Upload a file to the server
    """
    url = f"{config.API_URL}upload"
    payload = {"body": "", "bucket": config.BUCKET_NAME, "key": file_name, "email": email}
    try:
        # Read and encode the file
        with open(file_name, "rb") as file:
            encoded_file = base64.b64encode(file.read()).decode("utf-8")
            payload["body"] = encoded_file
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")
        return False

    try:
        # Send a request to the API endpoint to upload the file
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        # Check if the email is verified
        if "statusCode" in data:
            if data["statusCode"] != 200:
                print(data["message"])
                return False
            return True
    except requests.exceptions.HTTPError as e:
        print(response)
        print(f"An error occurred while uploading the file: {e}")
        return False
