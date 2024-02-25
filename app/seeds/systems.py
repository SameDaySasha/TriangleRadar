from app.models import db, Player, System, ThreatLevel
from app.models.db import environment, SCHEMA
from sqlalchemy import text
import json

# Load JSON data from a file
def load_json_data():
    with open('/Users/alexflorea/Desktop/Kyber_dar/practice-for-week-19-python-project-skeleton/app/seeds/systems.json', 'r') as file:
        return json.load(file)

def get_system_id_mapping():
    systems = System.query.all()
    return {system.name: system.id for system in systems}

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
            notes="{}"  # Initialize with empty JSON object/string
        )
        db.session.add(system)
    db.session.commit()

    # Then, update systems with connections using the name to ID mapping
    name_to_id = get_system_id_mapping()
    for node in json_data['nodes']:
        system = System.query.filter_by(name=node['name']).first()
        if system:
            # Prepare connections with system IDs instead of names
            connections = node['connections']
            connections['forward'] = [name_to_id.get(name) for name in connections.get('forward', []) if name in name_to_id]
            connections['back'] = name_to_id.get(connections.get('back'), None)
            connections['additional'] = [name_to_id.get(name) for name in connections.get('additional', []) if name in name_to_id]
            
            # Update the system's notes field or a dedicated connections field if available
            system.notes = json.dumps(connections)
    db.session.commit()

def undo_systems():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.systems RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM systems"))
    db.session.commit()

# Ensure to call seed_systems() in your seed management script or command