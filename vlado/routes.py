from flask import render_template, send_from_directory

from . import app
from .db import get_db


@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory(app.root_path + '/static/css/', filename)


@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory(app.root_path + '/static/js/', filename)


@app.route('/img/<path:filename>')
def img(filename):
    return send_from_directory(app.root_path + '/static/img/', filename)


@app.route('/vendor/<path:filename>')
def vendor(filename):
    return send_from_directory(app.root_path + '/static/vendor/', filename)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/adm')
def adm():
    pages = get_db().cursor().execute(
        'SELECT id, url FROM article'
    ).fetchall()
    return render_template('adm/index.html', pages=pages)


@app.route('/adm/<int:article_id>')
def adm_article_id(article_id):
    article = get_db().cursor().execute(
        'SELECT * FROM article WHERE id=:article_id',
        {
            'article_id': article_id,
        }
    ).fetchone()
    return render_template('adm/index.html', article=article)
