from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired, Length


class ContactUsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), InputRequired(), Length(min=3)])
    lastname = StringField('Last Name', validators=[DataRequired(), InputRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email(), InputRequired(), Length(min=13)])
    subject = StringField('Subject', validators=[DataRequired(), InputRequired()])
    message = TextAreaField('Message', validators=[DataRequired(), InputRequired()])
    submit = SubmitField('Send')

class SubscriberForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), InputRequired()])
    email = EmailField('Email', validators=[DataRequired(), InputRequired(), Length(min=13)])
    submit = SubmitField('Subscribe')
