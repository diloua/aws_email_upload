import sys
sys.path.append("../")
import requests_mock
import unittest
import upload_file
import config

class TestUploadFile(unittest.TestCase):
    def test_upload_file_success(self):
        with requests_mock.Mocker() as mock:
            mock.post(config.API_URL + "upload", json={'statusCode': 200})
            result = upload_file.uploadFile("file.txt", "test@example.com")
            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

