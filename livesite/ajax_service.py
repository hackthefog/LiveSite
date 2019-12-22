from livesite import app
from flask import render_template, redirect, url_for

def update_template_post(template, recent_post=None):
	# with app.app_context():
	# 	redirect(url_for('update_recent_posts'), recent_post=post)
	raise StatusDenied