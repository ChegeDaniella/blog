from flask import render_template,redirect,abort,url_for,flash,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog
from .forms import UpdateProfile,PostForm
from .. import db
import urllib.request as request
import json


@main.route('/')
def index():
    posts = Blog.query.all()
    return render_template('index.html', posts=posts)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update', methods = ['GET','POST'])
@login_required   
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form=UpdateProfile()

    if form.validate_on_submit():
        current_user.bio = form.bio.data
        current_user.location = form.location.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username)) 
    return render_template('profile/update.html', form = form)    

@main.route("/post/new",methods = ['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():

        blog = Blog(title = form.title.data, blog =form.content.data, author=current_user)

        db.session.add(blog)
        db.session.commit()
        flash('Your post has been created')
        return redirect(url_for('main.index'))
    return render_template('create_post.html',title ="New post" , form = form)

@main.route("/post/<int:post_id>")
def post(post_id):
    post = Blog.query.get_or_404(post_id)
    # post_id = request.args.get('id')
    return render_template('post.html', title=post.title, post=post)

@main.route("/post/<int:post_id>/update",methods = ['GET','POST'])
@login_required
def update_post(post_id):  
    post = Blog.query.get_or_404(post_id)  
    if post.author != current_user:
        abort(403)
    form =PostForm() 
    

    if form.validate_on_submit():
        post.title = form.title.data
        post.blog = form.content.data

        db.session.commit()
        flash('You have made updates to this post','success')
        return redirect(url_for('main.post', post_id=post.id))

    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.blog

    return render_template('create_post.html',title ="Update post" , form = form)

@main.route("/post/<int:post_id>/delete",methods = ['POST'])
@login_required
def delete_post(post_id):   
    post = Blog.query.get_or_404(post_id)  
    if post.author != current_user:
        abort(403)  
    db.session.delete(post) 
    db.session.commit()
    flash('You have made updates to this post','success')
    return redirect(url_for('main.index'))

@main.route("/random")
def random_quotes():
    # quote_data = request.json.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    # maker = quote_data.get('author')
    # quote = quote_data.get('quote')
        with request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as response:
            if response.getcode() == 200:
                source = response.read()
                data = json.loads(source)
            else:
                print('An error occurred while attempting to retrieve data from the API.')

        return render_template('random.html',data =data)