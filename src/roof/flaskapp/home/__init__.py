from flask import Blueprint

bp = Blueprint("home", __name__)

from roof.flaskapp.home import routes