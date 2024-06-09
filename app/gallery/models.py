from app import db 
from sqlalchemy.sql import func


class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    #media_type = db.Column(db.String(10), nullable=False)
    data_uploaded = db.Column(db.DateTime(timezone=True), default=func.now())


