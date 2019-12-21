from firebase_admin import auth
import hashlib

def create_post(title, content, time, imageurl=None):
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