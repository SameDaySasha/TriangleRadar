from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Player  # Updated import

def player_exists(form, field):
    # Checking if player exists by email
    email = field.data
    player = Player.query.filter(Player.email == email).first()
    if not player:
        raise ValidationError('Email provided not found.')

def password_matches(form, field):
    # Checking if password matches for the player
    password = field.data
    email = form.data['email']
    player = Player.query.filter(Player.email == email).first()
    if not player:
        raise ValidationError('No such player exists.')
    if not player.check_password(password):  # Ensure Player model has check_password method
        raise ValidationError('Password was incorrect.')

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email(), player_exists])
    password = StringField('password', validators=[DataRequired(), password_matches])
