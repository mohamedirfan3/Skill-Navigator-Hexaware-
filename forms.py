from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email ID', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    degree = StringField('Degree', validators=[DataRequired()])
    specialization = StringField('Specialization', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    certifications = StringField('Certifications (comma separated)')
    internship = StringField('Internship Details')
    courses = StringField('Courses Completed')
    linkedin = StringField('LinkedIn Profile Link')
    github = StringField('GitHub Profile Link')
    languages = StringField('Programming Languages Known')
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = EmailField('Email ID', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
