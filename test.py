import unittest
import upload_file

class TestUploadFile(unittest.TestCase):
    def test_upload_file_success(self):
        # Test a successful file upload
        result = upload_file.uploadFile('file.txt', 'no.reply.epilot.test@gmail.com')
        self.assertFalse(result)


    def test_upload_file_failure(self):
        # Test a failed file upload
        result = upload_file.uploadFile('nonexistent_file.txt', 'test@example.com')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
