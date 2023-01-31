#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template


app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 5000


@app.route("/", strict_slashes=False)
def index():
    """Render the template for the '/' route"""
    return render_template('0-index.html')


def start(app):
    """Start the flask app
    """
    app.run(host=HOST, port=PORT)


if __name__ == '__main__':
    start(app)
