from flask import send_from_directory

from . import app


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
