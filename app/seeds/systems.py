from app.models import db, Player, System, ThreatLevel
from app.models.db import environment, SCHEMA
from sqlalchemy import text

def seed_systems():
    # Systems with medium threat level
    medium_threat_systems = ["Niarja", "Kino", "Archee"]
    # All other systems are considered high threat level
    high_threat_systems = [
        "Vale", "Ala", "Wirashoda", "Senda", "Ahtila", "Kuharah",
        "Tunudan", "Harva", "Raravoss", "Skarkon", "Nani", "Urhinichi",
        "Otanuomi", "Kraild", "Konola", "Nalvula", "Angymonne", "Ichoriya",
        "Kaunokka", "Arvasaras", "Sakenta", "Komo", "Ignebaener", "Otela"
    ]
    
    # Seed medium threat level systems
    for system_name in medium_threat_systems:
        system = System(
            name=system_name,
            status="Active",
            threat_level=ThreatLevel.medium,
            notes="Initial seeding."
        )
        db.session.add(system)
    
    # Seed high threat level systems
    for system_name in high_threat_systems:
        system = System(
            name=system_name,
            status="Active",
            threat_level=ThreatLevel.high,
            notes="Initial seeding."
        )
        db.session.add(system)
        
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
