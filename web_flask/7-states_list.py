#!/usr/bin/python3
""" Function to start a Flash Web Application """
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Functon to remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Function to display a HTML page with a list of states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
