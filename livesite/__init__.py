# App imports
from flask import Flask
import config
import firebase_admin
from firebase_admin import credentials
from livesite.firebaseauth import *

# Create Firebase default version
InitializeFirebaseAdmin()

# Create Flask app
app = Flask(__name__)

# Add Configurations to app
app.config.from_pyfile('config.py', silent=True)

# Import all views
import livesite.views
