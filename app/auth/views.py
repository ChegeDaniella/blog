from flask import render_template,redirect,url_for,flash
from . import auth
from ..models import User
from .forms import SignUpForm,LoginForm
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
    return render_template('auth/signup.html' ,signup_form=form)

@auth.rote('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data)
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next')or url_for('main.index'))

        flash('Invalid email or password')

    title = "Where to login"
    return render_template("auth.login.html", login_form = login_form title = title)    