import mock
import unittest
import upload_file
import config

class TestUploadFile(unittest.TestCase):
    def test_upload_file_success(self):
        with requests_mock.Mocker() as mock:
            mock.post(config.API_URL + "upload", json={'statusCode': 200})
            result = upload_file.uploadFile("file.txt", "test@example.com")
            self.assertTrue(result)

    def test_upload_file_failure(self):
        with requests_mock.Mocker() as mock:
            mock.post(config.API_URL + "upload", json={'statusCode': 400, 'message': 'Bad Request'})
            result = upload_file.uploadFile("file.txt", "test@example.com")
            self.assertFalse(result)

    def test_upload_file_exception(self):
        with requests_mock.Mocker() as mock:
            mock.post(config.API_URL + "upload", exc=requests.exceptions.RequestException)
            result = upload_file.uploadFile("file.txt", "test@example.com")
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

