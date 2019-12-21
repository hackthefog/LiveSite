import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import exceptions
from firebase_admin import db

from livesite.confidential.secret_data import db_url

def initialize_admin_credientials():
	import os
	path = os.path.dirname(os.path.abspath(__file__))
	cred = credentials.Certificate(path + "/confidential/htf-live-firebase-adminsdk-ilojf-8e3541b3a1.json")
	fir_app = firebase_admin.initialize_app(cred, {
		'databaseURL': db_url
		})
	return fir_app
	# firebase_admin.delete_app(fir_app)

def initialize_basic_credientials():
	import os
	path = os.path.dirname(os.path.abspath(__file__))
	cred = credentials.Certificate(path + "/confidential/htf-live-firebase-adminsdk-ilojf-8e3541b3a1.json")
	fir_app = firebase_admin.initialize_app(cred, {
		'databaseURL': db_url,
		'databaseAuthVariableOverride': {
	    	'uid': 'my-service-worker'
	    }
	}, name='basic')
	return fir_app
	# firebase_admin.delete_app(fir_app)
   