#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index(strict_slashes=False):
    return "Hello HBNB!"
if __name__ == "__main__":
    app.run(debug=True)