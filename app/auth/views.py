from flask import render_template,redirect,url_for
from . import auth
from ..models import User
from .forms import SignUpForm
from .. import db

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/signup', methods = ['GET','POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(email = form.email.data , username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "This is a new account"
    return render_template('auth/signup.html' ,signup=form)