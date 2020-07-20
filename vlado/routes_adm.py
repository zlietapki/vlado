import os
import os.path
import re
import json

from flask import render_template, request, redirect
from werkzeug.utils import secure_filename

from . import app, common, db


@app.route('/adm')
def adm_index_handler():
    article = db.get_article_by_url('/me')
    return redirect(f'/adm/{article["id"]}')


@app.route('/adm/upload-image', methods=['POST'])
def upload_image():
    if 'file' in request.files.keys():
        file = request.files['file']
        filename = secure_filename(file.filename)
        local_filepath = os.path.join(app.root_path, 'static', 'img', 'upload', filename)
        file.save(local_filepath)
        web_filepath = os.path.join('/', 'img', 'upload', filename)

    return json.dumps({'location': web_filepath})


@app.route('/adm/uploaded-images-list')
def uploaded_images_list():
    upload = os.path.join(app.root_path, 'static', 'img', 'upload')
    img_list = []
    for file in os.listdir(upload):
        if file == '_empty':
            continue
        img_list.append({
            'title': file,
            'value': os.path.join('/img/upload', file),
        })
    return json.dumps(img_list)


@app.route('/adm/<int:article_id>', methods=['GET', 'POST'])
def adm_article_id_handler(article_id):
    if request.method == 'POST':
        text = request.form['article_text']
        db.save_article(article_id, text)

    article = db.get_article(article_id)
    data = {
        'article': article,
    }
    common.adm_add_common(data, request.path)
    return render_template('adm/page.html', **data)


@app.route('/adm/21', methods=['GET', 'POST'])  # /me/kosijerevo/galereja
@app.route('/adm/7', methods=['GET', 'POST'])  # /ru/kosijerevo/galereja
@app.route('/adm/27', methods=['GET', 'POST'])  # /me/somina/galereja
@app.route('/adm/13', methods=['GET', 'POST'])  # /ru/somina/galereja
@app.route('/adm/16', methods=['GET', 'POST'])  # /me/kosijerevo/igumen-i-monah
@app.route('/adm/2', methods=['GET', 'POST'])  # /ru/kosijerevo/igumen-i-monah
@app.route('/adm/23', methods=['GET', 'POST'])  # /me/somina/igumen-i-monahinie
@app.route('/adm/9', methods=['GET', 'POST'])  # /ru/somina/igumen-i-monahinie
def adm_gallery_handler():
    if request.method == 'POST':
        gallery_id = request.form['gallery_id']
        f = request.files['file']
        _, file_ext = os.path.splitext(f.filename)
        if file_ext.lower() in ['.jpg', '.png']:
            f_name = secure_filename(f.filename)
            full_name = os.path.join(app.root_path, 'static', 'img', f'gallery_{gallery_id}', f_name)
            f.save(full_name)

    url = request.path
    m = re.search(r'\d+$', url)
    gallery_id = m.group(0)

    article = db.get_article(gallery_id)

    imgs = common.get_gallery_imgs(gallery_id)
    data = {
        'imgs': imgs,
        'article': article,
    }
    common.adm_add_common(data, request.path)
    return render_template('adm/gallery.html', **data)


@app.route('/adm/delete-image', methods=['POST'])
def adm_delete_image_handler():
    img_path = request.form["image_path"]
    img_path = re.sub(r'^/', '', img_path)
    file_del = os.path.join(app.root_path, 'static', img_path)
    os.unlink(file_del)
    return 'ok'
