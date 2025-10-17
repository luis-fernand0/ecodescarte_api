from flask import Blueprint
from controllers.users import get_users
from controllers.cadastrar import cadastrar

routes_bp = Blueprint("routes", __name__)

routes_bp.route("/users", methods=["GET"])(get_users)
routes_bp.route("/cadastrar", methods=["POST"])(cadastrar)