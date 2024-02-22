from flask import Blueprint
from app.models import System
from flask import jsonify
from .db import db  # Make sure this import is correctly pointing to your db instance

system_routes = Blueprint('systems', __name__)

@system_routes.route('/')
def get_systems():
    systems = System.query.all()  # Query all systems from the database
    systems_list = [system.to_dict() for system in systems]  # Convert each system object to a dictionary
    return jsonify(systems_list)  # Return the list of systems as a JSON response

    from flask import request, abort  # Import abort to handle not found errors

@system_routes.route('/<int:system_id>')  # Dynamic route to get a system by its ID
def get_system(system_id):
    system = System.query.get(system_id)  # Query the database for the system with the given ID
    if system is None:
        abort(404)  # Return a 404 Not Found error if the system doesn't exist
    return jsonify(system.to_dict())  # Return the system as a JSON response if found
