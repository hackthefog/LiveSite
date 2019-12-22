from livesite import app
from flask import render_template, redirect, url_for, request
from firebase_admin import auth
from livesite.authentication import initialize_admin_credientials, initialize_basic_credientials
from livesite.fir_db import get_database_ref, add_new_data, retrieve_data_in_order, retrieve_data_latest
from livesite.post_model import create_post
from time import time

# Views
@app.route("/", methods=['GET'])
@app.route("/index", methods=['GET'])
@app.route("/index/", methods=['GET'])
@app.route("/home", methods=['GET'])
@app.route("/home/", methods=['GET'])
def index():
	ref = get_database_ref()
	post = retrieve_data_latest(ref)
	return render_template('home.html', recent_post=post)

@app.route("/announcements", methods=['GET'])
def announcements():
	ref = get_database_ref()
	data_post = create_post('Merry Christmas', "This is the most recent post", time())
	status = add_new_data(ref, data_post, access='admin')
	print(status)
	posts = retrieve_data_in_order(ref)
	for post in posts:
		print(post.time)
	return "hello"
# Error Handelers
@app.errorhandler(404)
def page_not_found(e):
    return 404

@app.route("/admin", methods=['GET', 'POST'])
def admin():
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