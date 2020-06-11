import os.path
import re
from os import listdir

from flask import current_app


def get_switch_url(url):
    match = re.search(r'/(\w+)', url)
    if not match.group(0):
        lang = current_app.config.get('INDEX_LANG', 'me')
    else:
        lang = match.group(1)

    if lang == 'me':
        switch_url = re.sub(r'^/\w+', '/ru', url, count=1)
    else:
        switch_url = re.sub(r'^/\w+', '/me', url, count=1)
    return switch_url


def get_gallery_imgs(gallery_id):
    gallery_path = 'vlado/static/img/gallery_' + gallery_id
    if not os.path.exists(gallery_path):
        os.mkdir(gallery_path)
    web_path = '/img/gallery_' + gallery_id + '/'
    imgs = [web_path + img for img in listdir(gallery_path)]
    return imgs
