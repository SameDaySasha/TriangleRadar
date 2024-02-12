from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Player  # Updated import to use Player

player_routes = Blueprint('players', __name__)  # Rename this to match the variable name used

@player_routes.route('/')
@login_required
def get_players():
    """
    Query for all players and returns them in a list of player dictionaries
    """
    players = Player.query.all()
    return jsonify({'players': [player.to_dict() for player in players]})  # Ensure Player model has a to_dict method

@player_routes.route('/<int:id>')
@login_required
def get_player(id):
    """
    Query for a player by id and returns that player in a dictionary
    """
    player = Player.query.get(id)
    if player:
        return jsonify(player.to_dict())  # Ensure Player model has a to_dict method
    return jsonify({'error': 'Player not found'}), 404


def to_dict(self):
    return {
        'id': self.id,
        'username': self.username,
        'email': self.email,
        # Include other fields as needed
    }
