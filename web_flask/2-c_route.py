#!/usr/bin/python3
""" Function to start a Flash Web Application C is FUN"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function to print a Message when / is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function to print a Message when /hbnb is called """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Function to print a Message when /c is called """
    return "C " + text.replace('_', ' ')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
