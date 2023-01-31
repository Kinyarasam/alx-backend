#!/usr/bin/env python3
"""A Basic Flask app
"""


from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Represents a Flask Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

HOST = '0.0.0.0'
PORT = 5000


@app.route('/', strict_slashes=False)
def index():
    """The home/index page.

    Returns:
        The rendered template of the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
