from __future__ import with_statement

import logging
from logging.config import fileConfig
import os

from flask import current_app
from alembic import context
from sqlalchemy import create_engine, text

# Ensure your environment variables are loaded
# You might need to load your .env file here if it's not loaded elsewhere
# from dotenv import load_dotenv
# load_dotenv()

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

SCHEMA = os.getenv("SCHEMA")

def get_engine():
    try:
        return current_app.extensions['migrate'].db.get_engine()
    except TypeError:
        return current_app.extensions['migrate'].db.engine

def create_schema_if_not_exists(engine, schema_name):
    if schema_name:
        with engine.connect() as conn:
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name}"))

def run_migrations_online():
    connectable = get_engine()

    if SCHEMA:
        create_schema_if_not_exists(connectable, SCHEMA)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=get_metadata(),
            process_revision_directives=process_revision_directives,
            version_table_schema=SCHEMA,  # Specify schema for Alembic version table if needed
            **current_app.extensions['migrate'].configure_args
        )

        with context.begin_transaction():
            context.run_migrations()

# Additional functions (get_metadata, process_revision_directives, etc.) remain unchanged

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
