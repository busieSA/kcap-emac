from app import db
from sqlalchemy.sql import func


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    event_date_time = db.Column(db.DateTime)
    location = db.Column(db.String(), nullable=False)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())

class AnnualEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    annual_event_date_time = db.Column(db.DateTime)
    location = db.Column(db.String(), nullable=False)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())
       

