from livesite import app
from flask import render_template, redirect, url_for


# Views
@app.route("/", methods=['GET'])
@app.route("/index", methods=['GET'])
@app.route("/index/", methods=['GET'])
@app.route("/home", methods=['GET'])
@app.route("/home/", methods=['GET'])
def index():
    return render_template('home.html')


@app.route("/puzzle", methods=['GET'])
@app.route("/puzzle/", methods=['GET'])
def puzzle():
    return render_template('puzzle.html')

# Error Handelers
@app.errorhandler(404)
def page_not_found(e):
    return 404
