from flask import Blueprint

education = Blueprint("education", __name__)

from . import views