import spacy
import os


##################
##SET PARAMETERS##
##################
params = {
    'model': 'kdtree_model_1.1.pkl',
    # 'vectorizer': , # Implemented as class below
    # 'clean_data': 'cannabis_clean_export_03.csv', # Not implemented
}

# Load spacy model

# Use if deploying to heroku.  manually add folder to base repo
#path_to_model = os.path.join(os.getcwd(), "en_core_web_md-2.2.0/")

# Use if local/pushing to github.  Requires installation of model via
#    python -m spacy download en_core_web_md
path_to_model = "en_core_web_md"
nlp = spacy.load(path_to_model)