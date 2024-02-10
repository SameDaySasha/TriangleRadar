from flask.cli import AppGroup
# Update the import paths according to your new file names and function names
from .players import seed_players, undo_players

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    # Assuming your environment handling logic remains the same
    if environment == 'production':
        # Before seeding in production, you might want to ensure that
        # all existing data is cleared to avoid conflicts or duplicates
        # This assumes you've updated your undo function accordingly
        undo_players()
        # Add a call to undo functions for other models here if necessary
    # Now calling the updated seed function for players
    seed_players()
    # Add calls to seed functions for other models here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    # Call the updated undo function for players
    undo_players()
    # Add calls to undo functions for other models here
