from livesite import app
from flask import render_template, redirect, url_for

recent_post = None

class StatusDenied(Exception):
    pass

@app.errorhandler(StatusDenied)
def redirect_on_status_denied(error):
    print("hello world")
    return redirect(url_for('update_recent_posts', recent_post=recent_post))

def update_template_post(post=None):
    # with app.app_context():
    # 	redirect(url_for('update_recent_posts'), recent_post=post)
    global recent_post
    recent_post = post
    raise StatusDenied