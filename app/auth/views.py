from flask import render_template,redirect,url_for
from . import auth
from ..models import User
from .forms import 

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@ath.route('/signup', methods = ['GET','POST'])    