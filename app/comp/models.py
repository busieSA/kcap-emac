from app import db
from sqlalchemy.sql import func


class Comp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='upcoming')  # 'upcoming', 'ongoing', 'completed'
    location = db.Column(db.String(100), nullable=True)
    max_participants = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Adding and image files here 

    filename = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Comp(id={self.id}, name={self.name}, date={self.date}, status={self.status})>"

