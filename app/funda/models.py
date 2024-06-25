from app import db
from sqlalchemy.sql import func

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())

    synopsis = db.relationship('Synopsis', backref='school', lazy=True, uselist=False)
    area = db.relationship('Area', backref='school', lazy=True, uselist=False)
    teachers = db.relationship('Teacher', backref='school', lazy=True)
    performers = db.relationship('Performer', backref='school', cascade='all, delete-orphan', overlaps="school_ref")

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    surname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())

    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=False)
    tel = db.relationship('Tel', backref='teacher', lazy=True, uselist=False)

class Tel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())

    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())
    
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))

class Synopsis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), nullable=False)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())

    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))

class Performer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    surname = db.Column(db.String(), nullable=False)
    age = db.Column(db.String(), nullable=False)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())

    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=False)

class Gender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    performers = db.relationship('Performer', backref='gender', lazy=True)
    teachers = db.relationship('Teacher', backref='gender', lazy=True)
