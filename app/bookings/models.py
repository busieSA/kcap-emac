from app import db 
from sqlalchemy.sql import func


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    