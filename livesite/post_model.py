from firebase_admin import auth
import hashlib
import time


def create_post(title, content, time, imageurl=None):
    '''
    Parameters:
            Title: String
            Content: String
            Time: Date object
            Imageurl: String
    Returns:
            JSON: dictionary of post
    '''
    post_id = hashlib.md5(str(time).encode('utf-8')).hexdigest()
    post = {
        post_id: {
            "title": title,
            "content": content,
            "time": time,
            "imageurl": imageurl
        }
    }
    return post


class Post(object):
    def __init__(self, data):
        self.title = data.get('title')
        self.content = data.get('content')
        self.time = time.strftime(
            '%Y-%m-%d %H:%M:%S',
            time.localtime(
                data.get('time')))
        self.float_time = data.get('time')
        self.imageurl = data.get('imageurl')  # may be null
