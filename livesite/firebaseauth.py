import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import exceptions

def InitializeFirbaseAdmin():
	import os
	path = os.path.dirname(os.path.abspath(__file__))
	cred = credentials.Certificate(path + "/confidential/htf-live-firebase-adminsdk-ilojf-8e3541b3a1.json")
	fir_app = firebase_admin.initialize_app(cred)
	# firebase_admin.delete_app(fir_app)
    