import unittest
from app.models import User,Blog,Comment
from app import db

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        self.new_comment = Comment(id = 1, comment="This is the comment",posted="12:30", user_id=1,blog_id=1)

    def tearDown(self):
        Comment.query.delete()    

    def test_check_instance(self):
        self.assertEquals(self.new_comment.id,1)
        self.assertEquals(self.new_comment.comment,"This is the comment")
        self.assertEquals(self.new_comment.posted,"12:30")     
        self.assertEquals(self.new_comment.user_id,1)  
        self.assertEquals(self.new_comment.blog_id,1)   

    def test_save_commment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)  

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12) 
        self.assertTrue(len(got_comments)== 1)       