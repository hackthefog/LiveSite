from hashlib import md5
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, email, password, id=None):
        self.id = id or md5(str(email).encode('utf-8')).hexdigest()
        self.email = email
        self.password = password

    def get_id(self):
        return self.id

    def __repr__(self):
        return "%d/%s" % (self.id, self.email)
