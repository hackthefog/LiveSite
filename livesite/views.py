from livesite import app
from flask import render_template, redirect, url_for, request
from firebase_admin import auth
from livesite.authentication import *
from livesite.fir_db import *
from livesite.post_model import *
from time import time

# Views
@app.route("/", methods=['GET'])
def index():
    return render_template('home.html')

@app.route("/announcements", methods=['GET'])
def announcements():
	ref = get_database_ref()
	data_post = create_post('Hello World', "Tis the season to be jolly", time())
	status = add_new_data(ref, data_post, access='admin')
	print(status)
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