from .db import db, environment, SCHEMA
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Enum
import enum

# Define an enumeration for threat_level if it's limited to specific values
class ThreatLevel(enum.Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class System(db.Model):
    __tablename__ = 'systems'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    threat_level = db.Column(Enum(ThreatLevel), nullable=False)
    last_reported = db.Column(db.DateTime, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

   

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'threat_level': self.threat_level.name,  # Assuming threat_level is an enum
            'last_reported': self.last_reported,
            'notes': self.notes,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
