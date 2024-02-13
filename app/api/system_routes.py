from flask import Blueprint
from app.models import System

system_routes = Blueprint('systems', __name__)

@system_routes.route('/')
def get_systems():
    # Your logic to retrieve and return systems
    pass