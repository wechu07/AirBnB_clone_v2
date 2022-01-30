#!/usr/bin/python3
'''
script that starts a Flask web application
'''

from flask import Flask, escape, request
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    ''' function to display Hello HBNB '''
    return f'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
