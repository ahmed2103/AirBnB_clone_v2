#!/usr/bin/python3
"""Starts flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def shutdown_session(exception):
    """close the sqlalchemy session"""
    storage.close()


@app.route('/states_list')
def states_list():
    """Renders the list of states in html templete"""
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0")