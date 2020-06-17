from flask import current_app, render_template, request

from . import app, common, db


@app.route('/')
@app.route('/<string:lang>')
@app.route('/<string:lang>/<path:_>')
def index_handler(lang=None, _=None):
    url = request.path
    if not lang:
        lang = current_app.config.get('INDEX_LANG', 'me')
        url = '/' + lang
    article = db.get_article_by_url(url)
    data = {
        'article': article,
    }
    common.page_add_common(data, request.path)
    return render_template('page.html', **data)


@app.route('/<string:_lang>/kosijerevo/galereja')
def gallery_handler(_lang=None):
    images = common.get_gallery_imgs(27)
    data = {
        'images': images,
    }
    common.page_add_common(data, request.path)
    return render_template('gallery.html', **data)
