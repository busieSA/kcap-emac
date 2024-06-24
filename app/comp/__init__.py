from flask import Blueprint

comp = Blueprint("comp", __name__)

from . import views

