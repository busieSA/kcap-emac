from flask import Blueprint

comp = Blueprint("compy", __name__)

from . import views

