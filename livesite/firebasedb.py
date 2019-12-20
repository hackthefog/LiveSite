import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://databaseName.firebaseio.com'
})