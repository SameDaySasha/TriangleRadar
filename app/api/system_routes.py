from flask import Blueprint
from flask_cors import CORS
from app.models import System, SystemFlag,db
from flask import jsonify
from flask import request, abort
from flask_login import current_user, login_required
system_routes = Blueprint('systems', __name__)

CORS(system_routes)



@system_routes.route('')
def get_systems():
    systems = System.query.all()  # Query all systems from the database
    systems_list = [system.to_dict() for system in systems]  # Convert each system object to a dictionary
    return jsonify(systems_list)  # Return the list of systems as a JSON response

  # Import abort to handle not found errors

@system_routes.route('/<int:system_id>')  # Dynamic route to get a system by its ID
def get_system(system_id):
    system = System.query.get(system_id)  # Query the database for the system with the given ID
    if system is None:
        abort(404)  # Return a 404 Not Found error if the system doesn't exist
    return jsonify(system.to_dict())  # Return the system as a JSON response if found
# get system flag route
@system_routes.route('/<int:system_id>/flags', methods=['GET'])
@login_required
def get_flags(system_id):
    system = System.query.get(system_id)
    if system is None:
        abort(404, description='System not found.')
    flags = SystemFlag.query.filter_by(system_id=system_id).all()
    return jsonify([flag.to_dict() for flag in flags]), 200

  
# create system flage route 
@system_routes.route('/<int:system_id>/flags', methods=['POST'])
@login_required
def create_flag(system_id):
    data = request.get_json()
    # You should validate your incoming data properly here.
    new_flag = SystemFlag(
        system_id=system_id,
        player_id=current_user.id,  # Assuming this is set by flask_login
        type=data['type'],
        description=data.get('description', ''),
        status=data.get('status', 'active')
    )
    db.session.add(new_flag)
    db.session.commit()
    return jsonify(new_flag.to_dict()), 201
  
  # update system flag route
@system_routes.route('/flags/<int:flag_id>', methods=['PUT'])
@login_required
def update_flag(flag_id):
    flag = SystemFlag.query.get(flag_id)
    if flag is None:
        abort(404, description='Flag not found.')
    if flag.player_id != current_user.id:
        abort(403, description='Not allowed to edit this flag.')
    
    data = request.get_json()
    # Again, validate your incoming data.
    flag.type = data['type']
    flag.description = data.get('description', flag.description)
    flag.status = data.get('status', flag.status)
    db.session.commit()
    return jsonify(flag.to_dict()), 200
  # delete system flag route
@system_routes.route('/flags/<int:flag_id>', methods=['DELETE'])
@login_required
def delete_flag(flag_id):
    flag = SystemFlag.query.get(flag_id)
    if flag is None:
        abort(404, description='Flag not found.')
    if flag.player_id != current_user.id:
        abort(403, description='Not allowed to delete this flag.')
    
    db.session.delete(flag)
    db.session.commit()
    return jsonify({'message': 'Flag deleted successfully'}), 200
