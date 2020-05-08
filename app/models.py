from . import db
from werkzeug.security import generate_password_hash,check_password_hash

#user table
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def __repr__(self):
        return f'User{self.username}'

#blog table
class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    blog = db.Column(db.String)
    time_in = db.Column(db.DateTime)
    users = db.relationship('User',backref = 'blog', lazy="dynamic")

    def __repr__(self):
        return f'User{self.title}'


