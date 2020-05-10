from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import date, datetime
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#user table
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),nullable =False)
    email = db.Column(db.String(255),unique = True, nullable = False)
    pass_secure = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String)
    location = db.Column(db.String(255))
    blogs = db.relationship('Blog',backref = 'author', lazy="dynamic")
    comments=db.relationship('Comment',backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)    

    def __repr__(self):
        return f'User{self.username}'

#blog table
class Blog(UserMixin,db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    blog = db.Column(db.String(255),nullable = False)
    time_in = db.Column(db.DateTime, nullable =False, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id') ,nullable = False)
    comment=db.relationship('Comment',backref='post',lazy='dynamic')


    def __repr__(self):
        return f'Blog{self.title}'

class Comment(UserMixin,db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String,nullable = False)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"),nullable = False)
    blog_id=db.Column(db.Integer,db.ForeignKey('blogs.id'),nullable = False) 

    def __repr__(self):
        return f"Comment ('{self.comment}','{self.user}')"

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog_id):
        comment=Comment.query.filter_by(blog_id=blog_id).all()
        return comment       


