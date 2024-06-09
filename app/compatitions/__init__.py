from flask import Blueprint

compatitions = Blueprint("compatitions", __name__)

from . import views