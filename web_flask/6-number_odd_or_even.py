#!/usr/bin/python3
"""Starts a new web app"""
from flask import Flask, abort, render_template

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
    """A string with a default value"""
    return f"Python {text}".replace('_', ' ')


@app.route("/number/<n>", strict_slashes=False)
def display_number(n):
    """Display number if it's a int"""
    if n.isdigit():
        n = int(n)
        return f"{n} is a number"
    else:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def return_number_template(n):
    """Display number in a webpage from a webapp"""
    if n.isdigit():
        n = int(n)
        return render_template('5-number.html', number=n)
    else:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def return_number_odd_even(n):
    """Display number in a webpage from a webapp"""
    if n.isdigit():
        n = int(n)
        if n % 2 == 0:
            condit = 'even'
        else:
            condit = 'odd'
        return render_template('6-number_odd_or_even.html',
                               number=n, condit=condit)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
