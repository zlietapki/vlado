from flask import Blueprint, render_template, request

from .db import get_db

bp = Blueprint('ru', __name__, url_prefix='/ru')


@bp.route('/<path:page>')
def handler(page):
    path = request.path
    row = (
        get_db()
        .execute(
            "SELECT * FROM article WHERE url = ?",
            (path,),
        )
        .fetchone()
    )
    return render_template('index.html', content=row['text'])


# @bp.route('/kosijerevo/crkva')
# def kos_crkva():
#     return render_template('index.html')


# @bp.route('/kosijerevo/kapela')
# def kos_kapela():
#     return render_template('index.html')


# @bp.route('/kosijerevo/istorija')
# def kos_history():
#     return render_template('index.html')


# @bp.route('/kosijerevo/dogadaji')
# def kos_events():
#     return render_template('index.html')


# @bp.route('/kosijerevo/galereja')
# def kos_gallery():
#     return render_template('index.html')


# @bp.route('/kosijerevo/kontakt')
# def kos_contact():
#     return render_template('index.html')


# @bp.route('/somina/igumen-i-monahinie')
# def somina_igumen():
#     return render_template('index.html')


# @bp.route('/somina/crkva')
# def somina_crkva():
#     return render_template('index.html')


# @bp.route('/somina/istorija')
# def somina_history():
#     return render_template('index.html')


# @bp.route('/somina/dogadaji')
# def somina_events():
#     return render_template('index.html')


# @bp.route('/somina/galereja')
# def somina_gallery():
#     return render_template('index.html')


# @bp.route('/somina/kontakt')
# def somina_contact():
#     return render_template('index.html')
