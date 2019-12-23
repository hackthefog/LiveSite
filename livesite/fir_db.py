from livesite.authentication import initialize_admin_credientials
from firebase_admin import db
from livesite.post_model import Post

def get_database_ref(ref='/'):
    '''
    Params:
        Reference: String stating where the db should start in json tree
    Returns:
        Reference: Reference object
    '''

    ref = db.reference(ref)

    return ref

def add_new_data(ref, data_dict, access='basic'):
    '''
    Params:
        Reference: location of data - '/posts'
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
        Reference: location of data - '/posts'
    Returns:
        Post: Post Objet
    '''
    posts = []
    snapshot = ref.child('posts').order_by_child('time').get()
    for key, val in snapshot.items():
        posts.insert(0, Post(val))
    return posts

def retrieve_data_latest(ref):
    '''
    Params:
        Reference: location of data - '/posts'
    Returns:
        Post: Post object containing the most recent post
    '''
    snapshot = ref.child('posts').order_by_child('time').limit_to_last(1).get()
    for key, val in snapshot.items():
        return Post(val)