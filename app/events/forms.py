from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField , SubmitField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    date = DateTimeField("Date and Time", format='%Y-%m-%d %H:%M:%S' ,validators=[DataRequired()])
    vanue = StringField("Location", validators=[DataRequired()]) 
    submit = SubmitField("Create Event")