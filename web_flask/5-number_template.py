#!/usr/bin/python3
"""Flask web application on 0.0.0.0 on port 5000."""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """triggers Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """triggers HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """displays c followed by value in text"""
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    """display “Python ”, followed by the value of the text variable """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """triggers content if n is integer only"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """triggers HTML page if n is integer only"""
    from flask import render_template
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
