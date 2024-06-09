from app import db
from sqlalchemy.sql import func


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


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_identification = db.Column(db.String(), unique=True)
    name = db.Column(db.String())
    description = db.String(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

class EventType():
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(), unique=True)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())



