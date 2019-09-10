'''
Put models, classes here
'''
from app import db, app
from datetime import datetime


class LiveEvents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow)

    def __repr__(self):
        return f"LiveEvents('{self.event}', '{self.date_posted}')"
