# Flask imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask app
app = Flask(__name__)

# Create DB
db = SQLAlchemy(app)

# Add Configurations to app
app.config.from_pyfile('config.py', silent=True)

# importing all the models and initializing them
from livesite.models import *
db.create_all()

# Import all views
import livesite.views
