from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

# creates and configures flask app
app = Flask(__name__)
# DB = SQLAlchemy() # Not Implemented

@app.route('/recommend/')
def root():
    #dump = pk.dumps('knn_05.pkl')
    #load = pk.loads('dump')
    values = randJSON()
    return values


if __name__ == "__main__":
    app.run(debug=True)