from .db import db, environment, SCHEMA
from sqlalchemy.types import JSON
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Enum
import enum

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
    status = db.Column(db.String(255), nullable=False)  # Assuming 'type' from JSON maps to 'status'
    threat_level = db.Column(Enum(ThreatLevel), nullable=False)
    connections = db.Column(JSON, default=dict)  # Storing connections as JSON
    last_reported = db.Column(db.DateTime, nullable=True)
    notes = db.Column(db.Text, nullable=True)  # Keep for additional textual notes
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'threat_level': self.threat_level.name,
            'connections': self.connections,  # Directly return the JSON/JSONB stored connections
            'last_reported': self.last_reported.isoformat() if self.last_reported else None,
            'notes': self.notes,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
