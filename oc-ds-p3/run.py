#! /usr/bin/env python
import flask_movies
from flask_movies import app
import pickle 

with open(app.config['SOURCE_FILE'], 'rb') as file: 
		unpickler = pickle.Unpickler(file)
		df = unpickler.load()

if __name__ == "__main__":
    app.run(debug=True)