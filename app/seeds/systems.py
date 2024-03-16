from app.models import db, System, ThreatLevel
from app.models.db import environment, SCHEMA
from sqlalchemy import text

def seed_systems():
    # Manually declare the systems and their connections
    systems_data = [
        {
            "name": "Archee",
            "status": "Active",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["filler"],
                "forward": ["Vale", "Angymonne"],
                "additional": ["filler"]
            },
            "notes": "{}"
        },
         {
            "name": "Angymonne",
            "status": "Internal",
            "threat_level":ThreatLevel.medium,  # Placeholder for threat level
            "connections": {
                "back": ["Archee", "Vale"],
                "forward": ["Ichoriya"],
                "additional": []
            },
            "notes": "{}"
        },
         {
            "name": "Ichoriya",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Angymonne"],
                "forward": ["Kaunokka"],
                "additional": []
            },
            "notes": "{}"
        },
            {
            "name": "Kaunokka",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Ichoriya"],
                "forward": ["Arvasaras"],
                "additional": []
            },
            "notes": "{}"
        },
          
        {
            "name": "Arvasaras",
            "status": "Border",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Kaunokka"],
                "forward": ["Sakenta"],
                "additional": []
            },
            "notes": "{}"
        },  
            
        {
            "name": "Sakenta",
            "status": "Border",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Arvasaras"],
                "forward": ["Komo"],
                "additional": []
            },
            "notes": "{}"
        },
        
        {
            "name": "Komo",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Sakenta"],
                "forward": ["Ignabaer"],
                "additional": []
            },
            "notes": "{}"
        },
          {
            "name": "Ignabaer",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Komo"],
                "forward": ["Otela"],
                "additional": []
            },
            "notes": "{}"
        },
           {
            "name": "Otela",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Ignabaer"],
                "forward": ["Kino", "Navula"],
                "additional": []
            },
            "notes": "{}"
        },
        {
            "name": "Kino",
            "status": "Home",  # Assuming status based on JSON type
            "threat_level": ThreatLevel.medium,  # Placeholder for threat level
            "connections": {
                "back": ["filler"],
                "forward": ["Otela", "Navula"],
                "additional": []
            },
            "notes": "{}"
        },       
         
        {
            "name": "Navula",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Kino", "Otela"],
                "forward": ["Konola"],
                "additional": []
            },
            "notes": "{}"
        },
        
        {
            "name": "Konola",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Navula"],
                "forward": ["Krirald"],
                "additional": []
            },
            "notes": "{}"
        },
        
        {
            "name": "Krirald",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Konola"],
                "forward": ["Otanuoumi"],
                "additional": []
            },
            "notes": "{}"
        },
         {
            "name": "Otanuoumi",
            "status": "Border",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Krirald"],
                "forward": ["Urhinichi"],
                "additional": []
            },
            "notes": "{}"
        },      
        {
            "name": "Urhinichi",
            "status": "Border",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Otanuoumi"],
                "forward": ["Nani"],
                "additional": []
            },
            "notes": "{}"
        },
    
        {
            "name": "Nani",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Urhinichi"],
                "forward": ["Skarkon"],
                "additional": []
            },
            "notes": "{}"
        },
     
        {
            "name": "Skarkon",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Nani"],
                "forward": ["Raravoss"],
                "additional": []
            },
            "notes": "{}"
        },
        {
            "name": "Raravoss",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Skarkon"],
                "forward": ["Niarja", "Harva"],
                "additional": []
            },
            "notes": "{}"
        },
         {
            "name": "Niarja",
            "status": "Home",  # Assuming status based on JSON type
            "threat_level": ThreatLevel.medium,  # Placeholder for threat level
            "connections": {
                "back": ["filler"],
                "forward": ["Harva", "Raravoss"],
                "additional": []
            },
            "notes": "{}"
        },
        {
            "name": "Harva",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Niarja", "Raravoss"],
                "forward": ["Tunudan"],
                "additional": []
            },
            "notes": "{}"
        },
        {
            "name": "Tunudan",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Harva"],
                "forward": ["Kuharah"],
                "additional": []
            },
            "notes": "{}"
        },
        {
            "name": "Kuharah",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Tunudan"],
                "forward": ["Ahtila"],
                "additional": []
            },
            "notes": "{}"
        },
        {
            "name": "Ahtila",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Kuharah"],
                "forward": ["Senda"],
                "additional": []
            },
            "notes": "{}"
        },
        {
            "name": "Senda",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Ahtila"],
                "forward": ["Niarja"],
                "additional": []
            },
            "notes": "{}"
        },
        {
            "name": "Wirashoda",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Niarja"],
                "forward": ["Ala"],
                "additional": []
            },
            "notes": "{}"
        },
        {
            "name": "Ala",
            "status": "Internal",
            "threat_level": ThreatLevel.medium,
            "connections": {
                "back": ["Wirashoda"],
                "forward": ["Vale"],
                "additional": []
            },
            "notes": "{}"
        },
          {
            "name": "Vale",
            "status": "Internal",
            "threat_level": ThreatLevel.high,
            "connections": {
                "back": ["Ala"],
                "forward": ["Archee", "Angymonne"],
                "additional": []
            },
            "notes": "{}"
        },
    ]

    for system_data in systems_data:
        system = System(
            name=system_data["name"],
            status=system_data["status"],
            threat_level=system_data["threat_level"],
            connections=system_data["connections"],
            notes=system_data["notes"]
        )
        db.session.add(system)
    db.session.commit()

def undo_systems():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.systems RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM systems"))
    db.session.commit()

# Ensure to call seed_systems() in your seed management script or command
