from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Player  # Updated import

def email_exists(form, field):
    # Checking if email is already in use by a player
    email = field.data
    player = Player.query.filter(Player.email == email).first()
    if player:
        raise ValidationError('Email address is already in use.')

def username_exists(form, field):
    # Checking if username is already in use by a player
    username = field.data
    player = Player.query.filter(Player.username == username).first()
    if player:
        raise ValidationError('Username is already in use.')

class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), username_exists])
    email = StringField(
        'email', validators=[DataRequired(), Email(), email_exists])
    password = StringField('password', validators=[DataRequired()])
