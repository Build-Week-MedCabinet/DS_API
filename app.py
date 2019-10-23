from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json
from nlp_module import nlp_model

###########
###Setup###
###########

# Create the application instance
app = Flask(__name__, template_folder="templates")
# DB = SQLAlchemy() # Not Implemented

# Initialize NLP Predictor
predictor = nlp_model.Predictor()


############
###Routes###
############
@app.route('/')
def root():
    return "API Main.  Use */api/recommend/"

@app.route('/api/recommend/', methods=['GET'])
def recommend():
    prediction = predictor.predict('Glorious orange-red sativa')
    return json.dumps(prediction)




if __name__ == "__main__":
    app.run(debug=True)