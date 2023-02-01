import sys
sys.path.append("../")
import requests_mock
import unittest
import verify_email
import config

class TestVerifyEmail(unittest.TestCase):
    def setUp(self):
        self.email = "test@example.com"

    @requests_mock.Mocker()
    def test_verify_email_success(self, mock_request):
        mock_request.post("/verifyEmail", json={"message": "Email has already been verified."}, status_code=200)
        result = verify_email.verifyEmail(self.email)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()

