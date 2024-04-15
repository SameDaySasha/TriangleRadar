"""FirstMigration

Revision ID: b4d333199f72
Revises: 
Create Date: 2024-04-15 11:04:23.225730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4d333199f72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('systems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('threat_level', sa.Enum('low', 'medium', 'high', name='threatlevel'), nullable=False),
    sa.Column('connections', sa.JSON(), nullable=True),
    sa.Column('last_reported', sa.DateTime(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_name', sa.String(length=255), nullable=False),
    sa.Column('character_id', sa.String(length=255), nullable=False),
    sa.Column('skill_points', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('last_known_location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['last_known_location_id'], ['systems.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('character_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('system_flags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('system_id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('OBS_SITE', 'SLEEPER_HOLE', 'HOME_FIELD', 'MINING_FIELD', 'BORDER', 'INTERNAL', 'ENEMY_SPOTTING', name='flagtype'), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], ),
    sa.ForeignKeyConstraint(['system_id'], ['systems.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('system_flags')
    op.drop_table('players')
    op.drop_table('systems')
    # ### end Alembic commands ###