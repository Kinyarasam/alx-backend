#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Render the template for the '/' route"""
    return render_template('0-index.html')


def start(app):
    """Start the flask app
    """
    app.run(host='0.0.0.0', port=5000)


start(app)
