from livesite import app
from flask import render_template, redirect, url_for
import pusher
from os import environ


# Views
@app.route("/", methods=['GET'])
def index():
    return render_template('home.html')

@app.route("/test", methods=['GET'])
def test():
    return 'Hello World'

# Error Handelers
@app.errorhandler(404)
def page_not_found(e):
    return 404