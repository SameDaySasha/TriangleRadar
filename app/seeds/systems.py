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
    # Checks if the environment variable is set to "production"
    if environment == "production":
        # Executes a TRUNCATE statement with the schema for production
        db.session.execute(f"TRUNCATE table {SCHEMA}.systems RESTART IDENTITY CASCADE;")
    else:
        # Executes a DELETE statement without a schema for development
        db.session.execute(text("DELETE FROM systems"))
    db.session.commit()
