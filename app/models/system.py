from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Enum
import enum

# Define an enumeration for threat_level if it's limited to specific values
class ThreatLevel(enum.Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class Player(db.Model, UserMixin):
    __tablename__ = 'players'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(255), nullable=False)
    character_id = db.Column(db.String(255), nullable=False, unique=True)  # Assuming character_id is unique
    skill_points = db.Column(db.Integer, nullable=False, default=0)
    last_known_location_id = db.Column(db.Integer, db.ForeignKey('systems.id'), nullable=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    deleted_at = db.Column(db.DateTime, nullable=True)

    # Relationship to the Systems table (if you have a Systems model)
    last_known_location = db.relationship('System', backref='players', lazy=True)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'character_name': self.character_name,
            'character_id': self.character_id,
            'skill_points': self.skill_points,
            'last_known_location_id': self.last_known_location_id,
            'username': self.username,
            'email': self.email
        }
