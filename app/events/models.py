from app import db
from sqlalchemy.sql import func






'''
class UserEvent(db.Model):
    __tablename__ = 'user_event'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('base_event.id'), primary_key=True)
    registration_date = db.Column(db.DateTime(timezone=True), nullable=False, default= func.utcnow())

    user = db.relationship("User", backref='user_event')
    base_event =db.relationship('BaseEvent', backref="user_event")

    __mapper_args__ = {
        'polymorphic_identity' : 'user_event',
        'polymorphic_on' : user_id, 
        'polymorphic_on' : event_id 

    }'''

user_event = db.Table("user_event",
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)


class BaseEvent(db.Model):
    __tablename__ = 'base_event'
    id = db.Column(db.Integer, primary_key=True)
    event_identification = db.Column(db.String(), unique=True)
    name = db.Column(db.String())
    description = db.String(db.Text())
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(), nullable=False)
    event_type = db.Column(db.String())
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    __mapper_args__ = {
        'polymorphic_identity' : 'base_event',
        'polymorphic_on' : event_type
    }

    user_id = db.relationship(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship('User', secondary='user_event', back_populates='events')

class Show(BaseEvent):
    __tablename__ = 'show'
    id = db.Column(db.Integer, db.ForeignKey('base_event.id'), primary_key=True)
    show_type = db.Column(db.String(150))
    __mapper_args__ = {
        'polymorphic_identity' : 'show'
    }

class Compatition(BaseEvent):
    __tablename__ = 'compatition'
    id = db.Column(db.Integer, db.ForeignKey('base_event.id'),primary_key=True )
    compatition_type = db.Column(db.String(150))
    __mapper_args__ = {
        'polymorphic_identity' : 'compatition'
    }

class AnnulEvent(BaseEvent):
    __tablename__ = 'anual_event'
    id = db.Column(db.Integer, db.ForeignKey('base_event.id'), primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    __mapper_args__ = {
        'polymorphic_identity' : 'anual_event'
    }

"""

class EventType():
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(), unique=True)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())

"""



class CompatitionEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_name = db.Column(db.String(), unique=True)
    comp_identification = db.Column(db.String(), unique=True)
    participant_age = db.Column(db.String(), nullable=True)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, entry_id, participant_name, participant_age, participant_email, competition_name, entry_date, entry_description, entry_score=None, is_winner=False):
        self.entry_id = entry_id
        self.participant_name = participant_name
        self.participant_age = participant_age
        self.participant_email = participant_email
        self.competition_name = competition_name
        self.entry_date = entry_date
        self.entry_description = entry_description
        self.entry_score = entry_score
        self.is_winner = is_winner

    def __str__(self):
        return f"Entry ID: {self.entry_id}, Participant: {self.participant_name}, Competition: {self.competition_name}, Date: {self.entry_date}, Score: {self.entry_score}, Winner: {self.is_winner}"

    def update_score(self, new_score):
        self.entry_score = new_score

    def mark_as_winner(self):
        self.is_winner = True

    def get_details(self):
        return {
            'entry_id': self.entry_id,
            'participant_name': self.participant_name,
            'participant_age': self.participant_age,
            'participant_email': self.participant_email,
            'competition_name': self.competition_name,
            'entry_date': self.entry_date,
            'entry_description': self.entry_description,
            'entry_score': self.entry_score,
            'is_winner': self.is_winner
        }





