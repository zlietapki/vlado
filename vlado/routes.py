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
@app.route('/<string:_lang>/somina/galereja')
def gallery_handler(_lang=None):
    url = request.path
    url2id = {
        '/ru/kosijerevo/galereja': 7,
        '/me/kosijerevo/galereja': 21,
        '/ru/somina/galereja': 13,
        '/me/somina/galereja': 27,
    }
    gal_id = url2id[url]
    images = common.get_gallery_imgs(gal_id)

    data = {
        'images': images,
    }
    common.page_add_common(data, request.path)
    return render_template('gallery.html', **data)
