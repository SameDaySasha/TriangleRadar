from __future__ import with_statement
import os
from dotenv import load_dotenv
load_dotenv()   # Load environment variables from .env file
import logging
from logging.config import fileConfig
from flask import current_app
from alembic import context




SCHEMA = os.getenv("SCHEMA")
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')


def get_engine():
    try:
        # this works with Flask-SQLAlchemy<3 and Alchemical
        return current_app.extensions['migrate'].db.get_engine()
    except TypeError:
        # this works with Flask-SQLAlchemy>=3
        return current_app.extensions['migrate'].db.engine


# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
config.set_main_option(
    'sqlalchemy.url', str(get_engine().url).replace('%', '%%'))
target_db = current_app.extensions['migrate'].db

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_metadata():
    if hasattr(target_db, 'metadatas'):
        return target_db.metadatas[None]
    return target_db.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=get_metadata(), literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


from sqlalchemy import create_engine, MetaData

from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine


# Assuming you've already loaded environment variables with dotenv


def create_schema_if_not_exists(engine: Engine, schema: str):
    if not engine.dialect.has_schema(engine, schema):
        engine.execute(f"CREATE SCHEMA {schema}")

def run_migrations_online():
    connectable = get_engine()

    if SCHEMA:
        create_schema_if_not_exists(connectable, SCHEMA)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # Ensure the schema is set here if necessary
            # e.g., version_table_schema=SCHEMA if using a specific schema for Alembic's version table
        )

        with context.begin_transaction():
            context.run_migrations()

