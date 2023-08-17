#!/usr/bin/python3
"""Starts a new web app"""
from flask import Flask, abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """A welcome page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """A HBNB page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """A custom page"""
    return f"C {text}".replace('_', ' ')


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def text2(text='is cool'):
    """A new custom page"""
    return f"Python {text}".replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
