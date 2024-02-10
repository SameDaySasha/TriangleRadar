from app.models import db, Player, environment, SCHEMA
from sqlalchemy.sql import text

# Adds demo players, you can add other players here if you want
def seed_players():
    demo = Player(
        username='Demo', 
        email='demo@aa.io', 
        password='password',
        character_name='DemoChar',
        character_id='1234567890',  # Assuming character IDs are strings
        skill_points=0,
        # Assuming you have a default system or NULL for last_known_location_id
    )
    marnie = Player(
        username='marnie', 
        email='marnie@aa.io', 
        password='password',
        character_name='MarnieChar',
        character_id='0987654321',
        skill_points=0,
    )
    bobbie = Player(
        username='bobbie', 
        email='bobbie@aa.io', 
        password='password',
        character_name='BobbieChar',
        character_id='1122334455',
        skill_points=0,
    )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the players table in production or DELETE in development
def undo_players():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.players RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM players"))
    db.session.commit()
