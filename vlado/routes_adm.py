import os
import os.path
import re

from flask import render_template, request
from werkzeug.utils import secure_filename

from . import app, common, db


@app.route('/adm')
def adm_index_handler():
    me_pages = db.get_me_pages()
    ru_pages = db.get_ru_pages()
    article = db.get_article_by_url('/me')
    return render_template('adm/page.html', me_pages=me_pages, ru_pages=ru_pages, article=article)


@app.route('/adm/<int:article_id>', methods=['GET', 'POST'])
def adm_article_id_handler(article_id):
    if request.method == 'POST':
        text = request.form['article_text']
        db.save_article(article_id, text)
    me_pages = db.get_me_pages()
    ru_pages = db.get_ru_pages()
    article = db.get_article(article_id)
    return render_template('adm/page.html', me_pages=me_pages, ru_pages=ru_pages, article=article)


@app.route('/adm/13', methods=['GET', 'POST'])
@app.route('/adm/27', methods=['GET', 'POST'])
def adm_gallery_handler():
    if request.method == 'POST':
        gallery_id = request.form['gallery_id']
        f = request.files['file']
        _, file_ext = os.path.splitext(f.filename)
        if file_ext.lower() in ['.jpg', '.png']:
            f_name = secure_filename(f.filename)
            full_name = f'vlado/static/img/gallery_{gallery_id}/{f_name}'
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
