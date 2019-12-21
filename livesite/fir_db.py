from livesite.authentication import *
from firebase_admin import db

def get_database_ref(ref='server/data'):

    ref = db.reference(ref)
    print(ref.get())

    return ref

def add_new_data(ref, data_dict, access='basic'):
    '''
    Params:
        Reference: location of data - 'server/data'
        Access: Admin or read only
        Data_dict: 
            Title: String,
            Content: String,
            Timestamp: Date
    Returns:
        False: Unsuccessful
        True: Successful
    '''

    if access == 'basic':
    	# No writing access with basic
        return False
    elif access == 'admin':
    	# Get the reference of the posts
        post_ref = ref.child('posts')
        # Attempt to write the new data to the db
        try:
            post_ref.update(data_dict)
            return True
        except Exception as e:
            print("Database Error: {0}".format(e))
            return False