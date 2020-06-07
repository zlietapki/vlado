import re

from flask import Blueprint, render_template, request

from . import db

bp = Blueprint('me', __name__, url_prefix='/me')
current_lang = 'me'


@bp.route('/<path:_page>')
def article_handler(_page):
    url = request.path
    article = db.article_by_url(url)
    switch_url = re.sub(r'/\w+', '/ru', url, count=1)
    return render_template('index.html', current_lang=current_lang, article=article, switch_url=switch_url)
