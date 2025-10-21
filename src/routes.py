from flask import Blueprint
from controllers.pontos import get_pontos
from controllers.cadastrar import cadastrar

routes_bp = Blueprint("routes", __name__)

routes_bp.route("/pontos", methods=["GET"])(get_pontos)
routes_bp.route("/cadastrar", methods=["POST"])(cadastrar)