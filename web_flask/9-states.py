#!/usr/bin/python3
""" lists all states and individual state """
from models.state import State
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """reloads storage"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """list of states"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """individual state"""
    key = "State." + id
    state = storage.all(State).get(key)
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
