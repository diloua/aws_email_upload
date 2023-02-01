import requests
import config

def verifyEmail(email: str) -> bool:
    """
    Verify the user email
    """
    url = f"{config.API_URL}verifyEmail"
    payload = {"email": email}
    try:
        # Send post request to verify email
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()

        # Check if email is already verified
        if "message" in data and data["message"] == config.EMAIL_VERIFIED_MSG:
            print("Email has already been verified, please proceed.")
            return True

        # Check for invalid email address
        elif "errorMessage" in data:
            print("Invalid email address.")
            return False
        print("Please validate the address email by following the steps in the email sent to you.")
        return True
    except requests.exceptions.HTTPError as e:
        print(f"An error occurred while trying to verify the email: {e}")
        return False

