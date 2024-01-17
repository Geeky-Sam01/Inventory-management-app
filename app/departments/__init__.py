from flask import Blueprint

departments_bp = Blueprint('departments', __name__)

from . import views