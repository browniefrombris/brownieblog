from wtforms.fields.simple import SubmitField
from app import app, db
from app.forms import LoginForm, PostForm
# from app.forms import DeleteContent
from app.models import Post, User
from flask import render_template, send_from_directory, url_for, flash, redirect
import os

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()
    user = {'username': 'Alexander'}

    if form.validate_on_submit():
        post = Post(body=form.post.data, author=User.query.get(1))
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    
    posts = Post.query.all()

    return render_template('index.html', title='Home', user=user, form=form, posts=posts)

@app.route('/clear_database', methods=['GET', 'POST'])
def clear_database():
    Post.query.delete()
    db.session.commit()
    return redirect(url_for('index'))



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'B_logo.ico', mimetype = 'image/png')

@app.route('/catalogue')
def catalogue():
	return render_template('catalogue.html')

@app.route('/fader')
def fader():
	return render_template('fader.html')

@app.route('/fader2')
def fader2():
	return render_template('fader2.html')

@app.route('/fader3')
def fader3():
	return render_template('fader3.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


