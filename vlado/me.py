from flask import Flask, escape, request, render_template
from flask import Blueprint
from .db import get_db

bp = Blueprint('me', __name__, url_prefix='/me')


@bp.route('/kosijerevo/igumen-i-monah')
def index():
    return render_template('index.html')
