from livesite import app
from flask import render_template, redirect, url_for
import pusher
from os import environ

# Views
@app.route("/", methods=['GET'])
def index():
	  channels_client = pusher.Pusher(
  	  	app_id=environ['PUSHER_ID'],
    		key=environ['PUSHER_KEY'],
    		secret=environ['PUSHER_SECRET'],
  		  cluster=environ['PUSHER_CLUSTER'],
  	  	ssl=True
	  )

	  channels_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
    return 200

# Error Handelers
@app.errorhandler(404)
def page_not_found(e):
    return 404