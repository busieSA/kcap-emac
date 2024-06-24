from app import db
from sqlalchemy.sql import func

class Enquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    subject = db.Column(db.String(), nullable=False)
    message = db.Column(db.String(), nullable=False)
    date_registered = db.Column(db.DateTime(timezone=True), default=func.now())

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)

"""
#important note can be  educational/compatition/opening/closing event ect, create relationship.
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    description = db.Column(db.String(), nullable=False)
    venue = db.Column(db.String(), nullable=False)
   # media_filename = db.Column(db.String(100))
    #event_date = db.Column(db.Date())
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

"""