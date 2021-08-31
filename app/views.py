from flask import jsonify, request
from app import app
from flask_pymongo import PyMongo, ObjectId
import json

app.config['MONGO_URI'] = 'mongodb://tide.csh.rit.edu/eric-recipes'
mongo = PyMongo(app, username="eric", password="password", tls=True)

def encoder(o):
    if type(o) == ObjectId:
        return str(o)
    return o.__str__

@app.route("/", methods=['GET'])
def index():
    return "Welcome to the recipe API! Try the /recipes route to get started and read some recipes! If only you could add new ones..."

@app.route("/recipes", methods=['GET', 'POST'])
def recipes():
    if request.method == 'POST':
        print(request.get_json(force=True))
        mongo.db.recipes.insert_one(request.json)
        return "Recipe added"
    return json.dumps(list(mongo.db.recipes.find()), default=encoder)
