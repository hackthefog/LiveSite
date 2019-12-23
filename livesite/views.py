from livesite import app
from flask import render_template, redirect, url_for, request
from firebase_admin import auth, db
from livesite.authentication import initialize_admin_credientials, initialize_basic_credientials
from livesite.fir_db import get_database_ref, add_new_data, retrieve_data_in_order, retrieve_data_latest
from livesite.post_model import create_post
from time import time
import threading


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

# Error Handelers
@app.errorhandler(404)
def page_not_found(e):
    return 404

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
			user = get_user_by_email(request.form['email'])
			# authenticated = is_user_authenticated(user, request.form['password'])
			return user.uid
	else:
		# send to login
		return render_template('admin.html')

@app.route("/admin/edit/add", methods=['GET', 'POST'])
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
		if request.form['title'] == None and request.form['content'] == None:
			ref = get_database_ref()
			data_post = create_post(request.form['title'], request.form['content'], time(), request.form.get('imageurl'))
			status = add_new_data(ref, data_post, access='admin')
			




