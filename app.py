from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from nlp_module import nlp_model

from errors import InvalidUsage

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
    # Set Defaults
    num_responses = 5

    if request.method == 'GET':
        if not 'search' in request.args:
            raise InvalidUsage(message="Search query not provided")
        if 'qty' in request.args:
            # print('number_responses', request.args['qty'])  # Debug
            num_responses = int(request.args['qty'])

    prediction = predictor.predict('Glorious orange-red sativa', size=num_responses)
    return {  # Can manually call jsonify().  Flask naturally conversts dicts to json objects.
        "predictions": prediction.tolist()
    }


# Register error handler
@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response



if __name__ == "__main__":
    app.run(debug=True)