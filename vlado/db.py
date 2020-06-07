import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def get_me_pages():
    me_pages = get_db().cursor().execute(
        'SELECT id, url FROM article WHERE lang="me"'
    ).fetchall()
    return me_pages


def get_ru_pages():
    ru_pages = get_db().cursor().execute(
        'SELECT id, url FROM article WHERE lang="ru"'
    ).fetchall()
    return ru_pages


def get_article(article_id):
    article = get_db().cursor().execute(
        'SELECT * FROM article WHERE id=:article_id',
        {
            'article_id': article_id,
        }
    ).fetchone()
    return article


def get_index_article(lang):
    article = get_db().cursor().execute(
        'SELECT * FROM article WHERE url=:article_url',
        {
            'article_url': '/' + lang,
        }
    ).fetchone()
    return article


def get_article_by_url(url):
    article = get_db().cursor().execute(
        'SELECT * FROM article WHERE url=:url',
        {
            'url': url,
        }
    ).fetchone()
    return article


def save_article(article_id, text):
    get_db().cursor().execute(
        'UPDATE article SET text=:text WHERE id=:id',
        {
            'text': text,
            'id': article_id,
        }
    )
    get_db().commit()
    return True
