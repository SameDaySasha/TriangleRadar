from app.models import db, Player, System, ThreatLevel
from app.models.db import environment, SCHEMA

def seed_systems():
    system1 = System(
        name="System Alpha",
        status="Active",
        threat_level=ThreatLevel.low,
        notes="Initial seeding."
    )
    
    system2 = System(
        name="System Beta",
        status="Active",
        threat_level=ThreatLevel.medium,
        notes="Initial seeding."
    )

    db.session.add(system1)
    db.session.add(system2)
    db.session.commit()

def undo_systems():
    db.session.execute('TRUNCATE systems RESTART IDENTITY CASCADE;')
    db.session.commit()
