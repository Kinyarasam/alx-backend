#!/usr/bin/env python3
"""A Basic Flask app
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Represents a Flask Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

HOST = '0.0.0.0'
PORT = 5000


@babel.localeselector
def get_locale():
    """Retrieves the locale for a web page

    Returns:
        The best match supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """The home/index page.

    Returns:
        The rendered template of the index page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
