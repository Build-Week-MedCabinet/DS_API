import spacy


##################
##SET PARAMETERS##
##################
params = {
    'model': 'kdtree_model_1.1.pkl',
    # 'vectorizer': , # Implemented as class below
    # 'clean_data': 'cannabis_clean_export_03.csv', # Not implemented
}

# Load spacy model
nlp = spacy.load("en_core_web_md")