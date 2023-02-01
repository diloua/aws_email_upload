import unittest
import requests_mock
import verify_email

class TestVerifyEmail(unittest.TestCase):
    def setUp(self):
        self.email = "test@example.com"

    @requests_mock.Mocker()
    def test_verify_email_success(self, mock_request):
        mock_request.post("/verifyEmail", json={"message": "Email has already been verified."}, status_code=200)
        result = verify_email.verifyEmail(self.email)
        self.assertTrue(result)

    @requests_mock.Mocker()
    def test_verify_email_failure(self, mock_request):
        mock_request.post("/verifyEmail", json={"errorMessage": "Invalid email address."}, status_code=400)
        result = verify_email.verifyEmail(self.email)
        self.assertFalse(result)

    @requests_mock.Mocker()
    def test_verify_email_http_error(self, mock_request):
        mock_request.post("/verifyEmail", exc=requests.exceptions.HTTPError)
        result = verify_email.verifyEmail(self.email)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

