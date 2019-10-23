from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import pickle as pk
import json
from random import randint

# creates and configures flask app
app = Flask(__name__)
DB = SQLAlchemy()

def randJSON():
    num1 = [randint(1,100) for _ in range(10)]
    num2 = [randint(1,100) for _ in range(10)]
    num3 = [randint(1,100) for _ in range(10)]
    x = {
        'set 1': num1,
        'set 2': num2,
        'set 3': num3
    }
    y = json.dumps(x)
    return y 


@app.route('/')
def root():
    #dump = pk.dumps('knn_05.pkl')
    #load = pk.loads('dump')
    values = randJSON()
    return values
   
#print(values)