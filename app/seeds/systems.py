from app.models import db, System, ThreatLevel
from app.models.db import environment, SCHEMA
from sqlalchemy import text
import json

# Load JSON data from a file
def load_json_data():
    with open('/Users/alexflorea/Desktop/Kyber_dar/practice-for-week-19-python-project-skeleton/app/seeds/systems.json', 'r') as file:
        return json.load(file)

def seed_systems():
    json_data = load_json_data()

    # First, create all systems without connections
    for node in json_data['nodes']:
        threat_level = ThreatLevel.high  # Default to high, adjust as necessary
        if node['name'] in ["Niarja", "Kino", "Archee"]:
            threat_level = ThreatLevel.medium

        system = System(
            name=node['name'],
            status="Active",  # Assuming 'type' in JSON maps to 'status' in the database
            threat_level=threat_level,
            connections={},  # Initialize connections with an empty dict
            notes="{}"  # Initialize with empty JSON object/string
        )
        db.session.add(system)
    db.session.commit()

    # Now, update systems with connections directly using names from the JSON
    for node in json_data['nodes']:
        system = System.query.filter_by(name=node['name']).first()
        if system:
            # Use names directly for 'forward', 'back', 'additional' connections
            system.connections = node['connections']
            db.session.add(system)  # Mark the system for update
    db.session.commit()

def undo_systems():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.systems RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM systems"))
    db.session.commit()

# Remember to call seed_systems() in your seed management script or command
