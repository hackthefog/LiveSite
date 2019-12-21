from livesite.authentication import initialize_admin_credientials
from firebase_admin import db
from livesite.post_model import Post

def get_database_ref(ref='/'):

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
            Time: Timestamp
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

def retrieve_data_in_order(ref):
    '''
    Params:
        Reference: location of data - 'server/data'
    Returns:
        Post: Post Objet
    '''
    posts = []
    snapshot = ref.child('posts').get()
    for key, val in snapshot.items():
        posts.append(Post(val))
    return posts

def retrieve_data_latest(ref):
    snapshot = ref.child('posts').order_by_child('time').limit_to_last(1).get()
    for key, val in snapshot.items():
        return Post(val)