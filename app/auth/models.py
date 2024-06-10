from app import db
from app.events.models import BaseEvent
from sqlalchemy.sql import func 
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    client_identification = db.Column(db.String(), unique=True)
    name = db.Column(db.String(), nullable=False)
    surname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    accept_tos = db.Column(db.String, nullable=False)
    date_registered = db.Column(db.DateTime(timezone=True), default=func.now())
    # Define the relationship with BaseEvent
    events = db.relationship('BaseEvent', backref='user', lazy=True)
    __mapper_args__ = {
        'polymorphic_identity' : 'user'
    }

    

