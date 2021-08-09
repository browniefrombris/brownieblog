from wtforms.fields.simple import SubmitField
from app import app, db
from app.forms import LoginForm, PostForm
# from app.forms import DeleteContent
from app.models import Post, User
from flask import render_template, send_from_directory, url_for, flash, redirect
import os


Post.query.delete()
db.session.commit()
redirect(url_for('index'))