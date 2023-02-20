#!/usr/bin/env python3
"""A Basic Flask app
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


class Config:
    """Represents a Flask Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Mock a database user table
users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spoky", "locale": "kg", "timezone": "Vulcan"},
        4: {
            "name": "Teletubby",
            "locale": "None",
            "timezone": "Europe/London"
            },
    }


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

HOST = '0.0.0.0'
PORT = 5000


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on the user id.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page

    Returns:
        The best match supported languages
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """The home/index page.

    Returns:
        The rendered template of the index page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
