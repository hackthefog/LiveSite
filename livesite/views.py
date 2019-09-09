from livesite import app
from flask import render_template, redirect, url_for

# Views
@app.route("/", methods=['GET'])
def index():
    return render_template('flask_index.html')

@app.route("/404", methods=['GET'])
def error_404():
    return render_template('404.html'), 404

# Error Handelers
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('error_404'))
