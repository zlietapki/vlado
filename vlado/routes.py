from flask import current_app, render_template, request, send_from_directory

from . import app, db


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
@app.route('/<string:current_lang>')
def index_handler(current_lang=None):
    if not current_lang:
        current_lang = current_app.config.get('INDEX_LANG', 'me')
    article = db.get_index_article(current_lang)
    switch_url = '/me'
    if current_lang == 'me':
        switch_url = '/ru'
    return render_template('index.html', current_lang=current_lang, article=article, switch_url=switch_url)


@app.route('/adm')
def adm():
    me_pages = db.get_me_pages()
    ru_pages = db.get_ru_pages()
    return render_template('adm/index.html', me_pages=me_pages, ru_pages=ru_pages)


@app.route('/adm/<int:article_id>', methods=['GET', 'POST'])
def adm_article_id(article_id):
    if request.method == 'POST':
        text = request.form['article_text']
        db.save_article(article_id, text)
    me_pages = db.get_me_pages()
    ru_pages = db.get_ru_pages()
    art = db.get_article(article_id)
    return render_template('adm/index.html', me_pages=me_pages, ru_pages=ru_pages, article=art)
