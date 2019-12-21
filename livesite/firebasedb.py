
def access_admin_db_privileges():
	'''
	Params:
		None
	Access 
	'''
	import firebase_admin
	from firebase_admin import credentials
	from firebase_admin import db
	# Initialize the app with a service account, granting admin privileges
	firebase_admin.initialize_app(cred, {
	    'databaseURL': 'https://databaseName.firebaseio.com'
	})

	ref = db.reference('restricted_access/secret_document')

	return ref

def access_read_db_privileges():
	'''
	Params:
		None
	Only able to read firebase database info
	'''
	import firebase_admin
	from firebase_admin import credentials
	from firebase_admin import db
	# Initialize the app with a service account, granting admin privileges
	firebase_admin.initialize_app(cred, {
	    'databaseURL': 'https://databaseName.firebaseio.com',
	    'databaseAuthVariableOverride': {
	    	'uid': 'my-service-worker'
	    }
	})

	ref = db.reference('/some_resource')

	return ref