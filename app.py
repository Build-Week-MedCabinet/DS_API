from flask import Flask, request, jsonify
from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy
from nlp_module import nlp_model
import os

from errors import InvalidUsage

###########
###Setup###
###########

# Update database name you want to connect to
local_db_name = "med_cabinet.sqlite3"

# Initialize NLP Predictor
predictor = nlp_model.Predictor()


#########################
###Application Factory###
#########################

# Create the application instance by calling create_app()
#     Example: app = create_app()

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, local_db_name),
        LOCALDATABASE=os.path.join(os.getcwd(), local_db_name)
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    import db
    db.init_app(app)


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

        # Get indices of strain from KDTree model
        prediction_indices = predictor.predict('Glorious orange-red sativa', size=num_responses)
        # Query database with those indices
        prediction_data = db.query_database(prediction_indices.tolist())

        return prediction_data


    # Register error handler
    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    return app


app = create_app()


if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)