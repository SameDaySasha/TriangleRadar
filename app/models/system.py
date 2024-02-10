from .db import db, environment, SCHEMA
from sqlalchemy.dialects.postgresql import ENUM as pgENUM

# Enum for threat levels, if you're using PostgreSQL
threat_level_enum = pgENUM('low', 'medium', 'high', name='threat_level_type', create_type=False)

class System(db.Model):
    __tablename__ = 'systems'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    status = db.Column(db.String(255), nullable=True)
    threat_level = db.Column(threat_level_enum, nullable=True)
    last_reported = db.Column(db.DateTime, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    # Relationships
    # Assuming you have other models that might reference `System`, e.g., `Player`
    players = db.relationship('Player', backref='system', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'threat_level': self.threat_level,
            'last_reported': self.last_reported,
            'notes': self.notes,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
