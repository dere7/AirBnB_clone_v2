#!/usr/bin/python3
"""starts a Flask web application"""
from models.place import Place
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """reloads storage"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """filtered index"""
    objs = {
        'states': storage.all(State).values(),
        'amenities': storage.all(Amenity).values(),
        'places': storage.all(Place).values()
    }
    return render_template('100-hbnb.html',**objs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
