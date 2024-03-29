import os

from flask import Flask, render_template, send_from_directory

from . import db

app = Flask(__name__, instance_relative_config=True)


def create_app(test_config=None):
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config['SECRET_KEY'] = 'qwdhwqd821'
        app.config['DATABASE'] = os.path.join(app.instance_path, 'vlado.sqlite')
        app.config['INDEX_LANG'] = 'me'
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    from . import routes_static
    from . import routes_adm
    from . import routes

    app.add_url_rule('/', endpoint="index_handler")

    return app
