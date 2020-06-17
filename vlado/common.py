import os.path
import re
from os import listdir

from flask import current_app

from . import db


def get_switch_url(url):
    match = re.search(r'/(\w+)', url)
    if match:
        lang = match.group(1)
    else:
        lang = current_app.config.get('INDEX_LANG', 'me')
        url = f'/{lang}'

    if lang == 'me':
        switch_url = re.sub(r'^/\w+', '/ru', url, count=1)
    else:
        switch_url = re.sub(r'^/\w+', '/me', url, count=1)
    return switch_url


def get_gallery_imgs(gallery_id):
    gallery_path = f'vlado/static/img/gallery_{gallery_id}'
    if not os.path.exists(gallery_path):
        os.mkdir(gallery_path)
    web_path = f'/img/gallery_{gallery_id}'
    imgs = [f'{web_path}/{img}' for img in listdir(gallery_path)]
    return imgs


def page_add_common(data, url):
    # lang
    if re.search(r'/me/', url):
        data['lang'] = 'me'
    else:
        data['lang'] = 'ru'

    # switch_url
    data['switch_url'] = get_switch_url(url)


def adm_add_common(data, url):
    data['me_pages'] = db.get_me_pages()
    data['ru_pages'] = db.get_ru_pages()
    data['path'] = url
