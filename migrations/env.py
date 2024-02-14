from __future__ import with_statement
import os
from dotenv import load_dotenv
import logging
from logging.config import fileConfig
from flask import current_app
from alembic import context
# Ensure your models are imported here if they're not automatically imported via the Flask app
from app.models import db  # Adjusted import to reflect your application structure

# Load environment variables
load_dotenv()

config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

# Function to retrieve the target metadata
def get_target_metadata():
    return db.metadata

# Set the 'target_metadata' for Alembic using the function.
target_metadata = get_target_metadata()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    # Logic to run migrations online
    connectable = config.attributes.get('connection', None) or current_app.extensions['sqlalchemy'].db.engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
            # Additional Alembic configurations can be set here (e.g., version_table_prefix)
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
