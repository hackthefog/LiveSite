from livesite import app
from flask import render_template, redirect, url_for

# Views
@app.route("/", methods=['GET'])
def index():
    return 200

# Error Handelers
@app.errorhandler(404)
def page_not_found(e):
    return 404