﻿import pandas as pd 
import numpy as np
import pickle 
from . import OC_DS_P3_fonctions as FKO 
from flask import Flask #, render_template, url_for, request
import json


app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

with open(app.config['SOURCE_FILE'], 'rb') as file: 
    unpickler = pickle.Unpickler(file)
    df = unpickler.load()
    cosine = unpickler.load()

#if __name__ == "__main__":
#    app.run() 

@app.route('/recommend/')
def recommend():
		return {'_result' : [{'ERR' : "Merci de renseigner un identifiant de film dans l'url"}]}

@app.route('/recommend2/')
def recommend2():
		return {'_result' : [{'ERR' : "Merci de renseigner un identifiant de film dans l'url"}]}

@app.route('/recommend/<string:ttid>/')
def recommend_id(ttid): 
		return json.dumps(FKO.similar_movies(df, ttid, app.config['NB_RECOS']), sort_keys=True, indent=4) 
		
@app.route('/recommend2/<string:ttid>/')
def recommend2_id(ttid):
		return json.dumps(FKO.similar_movies2(df, ttid, app.config['NB_RECOS'], cosine), sort_keys=True, indent=4)
