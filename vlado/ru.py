import re

from flask import Blueprint, render_template, request

from . import db

bp = Blueprint('ru', __name__, url_prefix='/ru')
current_lang = 'ru'


@bp.route('/<path:page>')
def article_handler(page):
    url = request.path
    article = db.article_by_url(url)
    switch_url = re.sub(r'/\w+', '/me', url, count=1)
    return render_template('index.html', current_lang=current_lang, article=article, switch_url=switch_url)
