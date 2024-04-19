#!/usr/bin/python3
"""Flask web application on 0.0.0.0 on port 5000."""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slaches=False)
def index():
    """triggers Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slaches=False)
def hbnb():
    """triggers HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
