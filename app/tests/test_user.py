import unittest
from app.models import User,Blog,Comment
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'James',password = 'rawnoodles', email='james@gmail.com')
        self.new_Blog= Blog(id = 1,title="new blog",blog="this is a blog",time_in='12:30',user_id=1)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance(self):
        self.assertEquals(self.new_James.username,"James")
        self.assertEquals(self.new_James.password,'rawnoodles')
        self.assertEquals(self.new_James.email,'james@gmail.com')

    def test_password_setter(self):
        self.assertTrue(self.new_James.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_James.password

    def test_password_verification(self):
        self.assertTrue(self.new_James.verify_password('rawnoodles'))                