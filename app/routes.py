from app import app
from flask import render_template, send_from_directory, url_for
import os

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Alexander'}
	return render_template('index.html', title='Home', user=user)

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

