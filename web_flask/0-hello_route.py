#!/usr/bin/python3
"""Starts a flask web application on the 0.0.0.0  litening to port 5000"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """displays welcome message"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
