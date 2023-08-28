#!/usr/bin/python3
"""Starts a new web app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close SQLAlchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """List of states"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """States sorted by id"""
    states = storage.all(State)
    cons_state = None
    obj_id = 0
    for k, v in states.items():
        obj_id = k.split('.')
        if obj_id[1] == id:
            cons_state = v
            break
    return render_template('9-states.html', states=cons_state, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
