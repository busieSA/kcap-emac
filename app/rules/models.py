from app import db
from sqlalchemy.sql import func


class rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Colmn(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)

    date_added = db.Column(db.DateTime(timezone=True), default=func.now())



