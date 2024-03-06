from app.models import db, System, ThreatLevel
from app.models.db import environment, SCHEMA
from sqlalchemy import text


def seed_systems():
    systems_data = [
        # Updated connections using IDs instead of names
        {
            "id": 0,
            "name": "Archee",
            "status": "Home",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [],
                "forward": [3, 4],  # Vale, Angymonne
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 1,
            "name": "Kino",
            "status": "Home",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [],
                "forward": [11, 12],  # Otela, Navula
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 2,
            "name": "Niarja",
            "status": "Home",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [],
                "forward": [20, 19],  # Harva, Raravoss
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 3,
            "name": "Vale",
            "status": "Internal",
            "threat_level": ThreatLevel.high,
            "connections": {
                "back": [26],  # Ala
                "forward": [0, 4],  # Archee, Angymonne
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 4,
            "name": "Angymonne",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [0, 3],  # Archee, Vale
                "forward": [5],  # Ichoriya
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 5,
            "name": "Ichoriya",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [4],  # Angymonne
                "forward": [6],  # Kaunokka
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 6,
            "name": "Kaunokka",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [5],  # Ichoriya
                "forward": [7],  # Arvasaras
                "additional": []
            },
            "notes": "{}"
        },
        # Continue updating the rest of the systems...
        {
            "id": 7,
            "name": "Arvasaras",
            "status": "Border",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [6],  # Kaunokka
                "forward": [8],  # Sakenta
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 8,
            "name": "Sakenta",
            "status": "Border",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [7],  # Arvasaras
                "forward": [9],  # Komo
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 9,
            "name": "Komo",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [8],  # Sakenta
                "forward": [10],  # Ignabaer
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 10,
            "name": "Ignabaer",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [9],  # Komo
                "forward": [11],  # Otela
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 11,
            "name": "Otela",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [10],  # Ignabaer
                "forward": [1, 12],  # Kino, Navula
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 12,
            "name": "Navula",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [1, 11],  # Kino, Otela
                "forward": [13],  # Konola
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 13,
            "name": "Konola",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [12],  # Navula
                "forward": [14],  # Krirald
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 14,
            "name": "Krirald",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [13],  # Konola
                "forward": [15],  # Otanuoumi
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 15,
            "name": "Otanuoumi",
            "status": "Border",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [14],  # Krirald
                "forward": [16],  # Urhinichi
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 16,
            "name": "Urhinichi",
            "status": "Border",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [15],  # Otanuoumi
                "forward": [17],  # Nani
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 17,
            "name": "Nani",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [16],  # Urhinichi
                "forward": [18],  # Skarkon
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 18,
            "name": "Skarkon",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [17],  # Nani
                "forward": [19],  # Raravoss
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 19,
            "name": "Raravoss",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [18],  # Skarkon
                "forward": [2, 20],  # Niarja, Harva
                "additional": []
            },
            "notes": "{}"
        },
         {
            "id": 20,
            "name": "Harva",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [2, 19],  # Niarja, Raravoss
                "forward": [21],  # Tunudan
                "additional": []
            },
            "notes": "{}"
        },
         {
            "id": 21,
            "name": "Tunudan",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [20],  # Harva
                "forward": [22],  # Kuharah
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 22,
            "name": "Kuharah",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [21],  # Tunudan
                "forward": [23],  # Ahtila
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 23,
            "name": "Ahtila",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [22],  # Kuharah
                "forward": [24],  # Senda
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 24,
            "name": "Senda",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [23],  # Ahtila
                "forward": [2],  # Niarja
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 25,
            "name": "Wirashoda",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [2],  # Niarja
                "forward": [26],  # Ala
                "additional": []
            },
            "notes": "{}"
        },
        {
            "id": 26,
            "name": "Ala",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": [25],  # Wirashoda
                "forward": [3],  # Vale
                "additional": []
            },
            "notes": "{}"
        }
    ]

    for system_data in systems_data:
        # Assuming your System model and db session are already configured to handle the schema based on the environment
        system = System(
            id=system_data["id"],
            name=system_data["name"],
            status=system_data["status"],
            threat_level=system_data["threat_level"],
            connections=system_data["connections"],
            notes=system_data["notes"]
        )
        db.session.add(system)
        db.session.commit()

def undo_systems():
    # Handling schema for production vs. other environments during undo operations
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.systems RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("TRUNCATE systems RESTART IDENTITY CASCADE;"))
    db.session.commit()