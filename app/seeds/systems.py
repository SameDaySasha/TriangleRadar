from app.models import db, Player
from app.models.db import environment, SCHEMA

def seed_systems():
    system1 = System(
        name="System Alpha",
        status="Active",
        threat_level=ThreatLevel.low,
        notes="Initial seeding."
    )

    db.session.add(system1)
    db.session.commit()

def undo_systems():
    db.session.execute('TRUNCATE systems RESTART IDENTITY CASCADE;')
    db.session.commit()
