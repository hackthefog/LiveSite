# App imports
from flask import Flask
from flask_login import LoginManager
import config
import firebase_admin
from firebase_admin import credentials
from livesite.authentication import *

# Create Firebase default version
fir_admin = initialize_admin_credientials()

# Create Flask app
app = Flask(__name__)

# Create login manager for admin
login_manager = LoginManager()
login_manager.init_app(app)

# Add Configurations to app
app.config.from_pyfile('../config.py', silent=True)

# Import all views
import livesite.views
