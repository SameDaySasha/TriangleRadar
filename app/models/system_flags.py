# system_flags.py
from .db import db, environment, SCHEMA
from enum import Enum

# If you are using an Enum for flag types, define it as follows
class FlagType(Enum):
    OBS_SITE = "OBS Site"
    SLEEPER_HOLE = "Sleeper Hole"
    HOME_FIELD = "Home Field"
    MINING_FIELD = "Mining Field"
    BORDER = "Border"
    INTERNAL = "Internal"
    ENEMY_SPOTTING = "Enemy Spotting"

class SystemFlag(db.Model):
    __tablename__ = 'system_flags'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    system_id = db.Column(db.Integer, db.ForeignKey('systems.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    type = db.Column(db.Enum(FlagType), nullable=False)  # Use your enum here
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), nullable=False, default="active")
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # Relation to System
    system_id = db.Column(db.Integer, nullable=False)
    # Relationship to System, using implicit backref from System model
    system = db.relationship('System', backref=db.backref('system_flags', lazy=True))

# Relationship to Player, using implicit backref from Player model
    player = db.relationship('Player', backref=db.backref('system_flags', lazy=True))


    # Relation to Player
    player_id = db.Column(db.Integer, nullable=False)
    def to_dict(self):
        return {
            "id": self.id,
            "system_id": self.system_id,
            "player_id": self.player_id,
            "type": self.type.name if self.type else None,  # Adjust this line if not using an Enum
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
