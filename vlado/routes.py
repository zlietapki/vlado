import os
import re
from werkzeug.utils import secure_filename
from flask import current_app, render_template, request, send_from_directory

from . import app, common, db
from .common import get_switch_url


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
@app.route('/<string:lang>')
@app.route('/<string:lang>/<path:_>')
def index_handler(lang=None, _=None):
    url = request.path
    if not lang:
        lang = current_app.config.get('INDEX_LANG', 'me')
        url = '/' + lang
    article = db.get_article_by_url(url)
    switch_url = get_switch_url(url)
    return render_template('page.html', lang=lang, switch_url=switch_url, article=article)


@app.route('/adm')
def adm_index_handler():
    me_pages = db.get_me_pages()
    ru_pages = db.get_ru_pages()
    article = db.get_article_by_url('/me')
    return render_template('adm/index.html', me_pages=me_pages, ru_pages=ru_pages, article=article)


@app.route('/adm/<int:article_id>', methods=['GET', 'POST'])
def adm_article_id_handler(article_id):
    if request.method == 'POST':
        text = request.form['article_text']
        db.save_article(article_id, text)
    me_pages = db.get_me_pages()
    ru_pages = db.get_ru_pages()
    article = db.get_article(article_id)
    return render_template('adm/index.html', me_pages=me_pages, ru_pages=ru_pages, article=article)


@app.route('/adm/13', methods=['GET', 'POST'])
@app.route('/adm/27', methods=['GET', 'POST'])
def adm_gallery_handler():
    if request.method == 'POST':
        gallery_id = request.form['gallery_id']
        print("gallery_id", gallery_id)
        f = request.files['file']
        f_name = secure_filename(f.filename)
        full_name = f'vlado/static/img/gallery_{gallery_id}/{f_name}'
        print(full_name)
        f.save(full_name)

    me_pages = db.get_me_pages()
    ru_pages = db.get_ru_pages()

    url = request.path
    m = re.search(r'\d+$', url)
    gallery_id = m.group(0)

    article = db.get_article(gallery_id)

    imgs = common.get_gallery_imgs(gallery_id)

    return render_template('adm/gallery.html', me_pages=me_pages, ru_pages=ru_pages, imgs=imgs, article=article)


@app.route('/adm/delete-image', methods=['POST'])
def adm_delete_image_handler():
    img_path = request.form["image_path"]
    os.unlink('vlado/static' + img_path)
    return 'ok'
