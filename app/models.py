from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))

    def __repr__(self):
        return f'User{self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    blog = db.Column(db.String)
    time_in = db.Column(db.DateTime)
    users = db.relationship('User',backref = 'blog', lazy="dynamic")

    def __repr__(self):
        return f'User{self.title}'


