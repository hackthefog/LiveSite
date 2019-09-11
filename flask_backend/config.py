# Import os
import os

# random for testing
SECRET_KEY = os.urandom(32)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	        			  'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_COMMIT_ON_TEARDOWN = True