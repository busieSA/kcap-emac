from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, BooleanField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length, EqualTo, Email

class RegisterUserForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired(), InputRequired()])
    surname = StringField('Last Name', validators=[DataRequired(), InputRequired()])
    email = EmailField('Email', validators=[DataRequired(), InputRequired(), Length(min=7), Email()])
    password = PasswordField('Password', validators=[DataRequired(), InputRequired(), Length(min=8),
                                                     EqualTo('confirm', message='Password must match!!')])
    confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    accept_tos = BooleanField('Accept Our Terms', validators=[DataRequired()])
    submit = SubmitField('Register')

class UserLoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), InputRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), InputRequired()])
    submit = SubmitField('Login')


