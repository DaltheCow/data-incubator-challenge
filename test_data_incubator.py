import os
import hello
import unittest
import tempfile
from io import BytesIO
# from io import StringIO

class DataIncubatorTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, hello.app.config['DATABASE'] = tempfile.mkstemp()
        hello.app.config['TESTING'] = True
        self.app = hello.app.test_client()
        # hello.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(hello.app.config['DATABASE'])

    def test_empty_db(self):
        with open('water-drops.png', 'rb') as img1:
            img1StringIO = BytesIO(img1.read())
        rv = self.uploadPhoto('water-drops.png')
        img1StringIO.seek(0)
        assert rv.data == img1StringIO.read()

    def uploadPhoto(self, file_name):
        with open(file_name, 'rb') as img2:
            img2StringIO = BytesIO(img2.read())
        data = dict(file=(img2StringIO, file_name))
        return self.app.post(
            '/images',
            data=data,
            content_type='multipart/form-data'
        )

if __name__ == '__main__':
    unittest.main()
