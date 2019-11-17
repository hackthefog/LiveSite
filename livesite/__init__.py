# Flask imports
from flask import Flask
import pyrebase
import config

# Create Flask app
app = Flask(__name__)

# Add Configurations to app
app.config.from_pyfile('config.py', silent=True)

# Create firebase object
firebase = pyrebase.initialize_app(config.firebase_config)

# Import all views
import livesite.views
