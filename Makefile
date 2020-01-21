init:
	pip3 install -r requirements.txt

update:
	pip install --upgrade pip setuptools wheel CacheControl cachetools certifi chardet Click firebase-admin Flask Flask-Login google-api-core google-api-python-client google-auth google-auth-httplib2 google-cloud-core google-cloud-firestore google-cloud-storage google-resumable-media googleapis-common-protos grpcio httplib2 idna itsdangerous Jinja2 MarkupSafe msgpack protobuf pyasn1 pyasn1-modules pytz requests rsa six uritemplate urllib3 Werkzeug
	pip freeze > requirements.txt

clean:
	pystarter clean

run:
	python3 run.py