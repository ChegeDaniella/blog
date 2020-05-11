import unittest
from app.models import Blog
from app import db

class BlogModelTest(unittest.TestCase):

    def setUp(self):
        self.new_Blog= Blog(id = 1,title="new blog",blog="this is a blog",time_in='12:30',user_id=1)

    def tearDown(self):
        Blog.query.delete()
         
    def test_check_instance(self):
        self.assertEquals(self.new_Blog.id,1)
        self.assertEquals(self.new_Blog.title,"new blog")
        self.assertEquals(self.new_Blog.blog,"this is a blog")     
        self.assertEquals(self.new_Blog.time_in,'12:30')  
        self.assertEquals(self.new_Blog.user_id,1)  