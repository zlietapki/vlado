import re

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
