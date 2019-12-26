from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user 
from livesite import app, login_manager
from livesite.authentication import initialize_admin_credientials, initialize_basic_credientials
from livesite.fir_db import get_database_ref, add_new_data, retrieve_data_in_order, retrieve_data_latest
from livesite.post_model import create_post
from livesite.confidential.login_credentials import *
from livesite.UserModel import User
from firebase_admin import auth, db
from time import time


# Views
@app.route("/", methods=['GET'])
@app.route("/index", methods=['GET'])
@app.route("/index/", methods=['GET'])
@app.route("/home", methods=['GET'])
@app.route("/home/", methods=['GET'])
def index():
	return render_template('home.html')

@app.route("/update_recent_posts", methods=["GET", "POST"])
def update_recent_posts():
	'''
	Reference - access to db
	Post - post object to return
	'''

	ref = get_database_ref()

	post = retrieve_data_latest(ref)

	return render_template('recent_post.html', recent_post=post)


@app.route("/announcements", methods=['GET'])
def announcements():
	return render_template('announcements.html')

@app.route("/update_all_posts")
def update_all_posts():
	'''
	Reference - access to db
	Post - post object to return
	'''

	ref = get_database_ref()

	posts = retrieve_data_in_order(ref)

	return render_template('announcements_loader.html', posts=posts)

@login_manager.user_loader
def load_user(user_id):
    return User(login_email, login_password, user_id)

@app.route("/admin/login", methods=['GET', 'POST'])
def admin_login():
	'''
	For admin login
	POST: 
		form['email']: String
		form['password']: String
	GET:
		Parameters: null
	'''
	if request.method == 'POST':
		# check if form is empty
		if request.form['email'] == None and request.form['password'] == None:
			# send back to login
			return render_template('admin.html')
		else:
			if request.form['email'] == login_email and request.form['password'] == login_password:
				user = User(request.form['email'], request.form['password'])
				login_user(user)
				return redirect(url_for('edit_new_data'))
			return render_template('admin.html')
	else:
		# send to login
		return render_template('admin.html')

@app.route("/admin/logout")
@login_required
def logout():
    logout_user()
    return "Logged out"

@app.route("/admin/edit/add", methods=['GET', 'POST'])
@login_required
def edit_new_data():
	'''
	For admin adding new posts
	POST:
		form['title']
		form['content']
		form['imageurl']
	GET:
		Parameters: null
		Return back to edit page
	'''
	if request.method == 'POST':
		form = request.form
		if form['title'] != None and form['content'] != None:
			ref = get_database_ref()
			data_post = create_post(form['title'], form['content'], time(), form.get('imageurl'))
			status = add_new_data(ref, data_post, access='admin')
			return f"Created post: Title-{form['title']}, Content-{form['content']}, Imageurl-{form.get('imageurl')}"
		return render_template('edit_new_data.html')
	elif request.method == 'GET':
		return render_template('edit_new_data.html')
			
@app.errorhandler(404)
def page_not_found(error):
    return "404"



