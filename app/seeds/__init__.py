from flask.cli import AppGroup
from .players import seed_players, undo_players
# Import seed and undo functions for the System model
from .systems import seed_systems, undo_systems
from app.models.db import environment, SCHEMA
from app.models import db, Player
from sqlalchemy.sql import text

from app.models.db import db, environment, SCHEMA

seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Assuming clearing data before seeding in production
        undo_players()
        undo_systems()  # Add this line
    seed_players()
    seed_systems()  # Add this line

@seed_commands.command('undo')
def undo():
    undo_players()
    undo_systems()  # Add this line
