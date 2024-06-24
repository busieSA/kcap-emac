from flask import Blueprint

rules = Blueprint("ruels", __name__)

from . import views
