from flask import Blueprint

funda = Blueprint('funda', __name__)

from . import views

#to add models as well for better relational mapping