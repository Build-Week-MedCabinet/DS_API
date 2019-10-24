import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """
    Returns current database connection.  If connection not present,
    initiates connection to configured database.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)

def queryDB(lst):
    import os
    
    os.chdir("D:\\Documents\\Build week projects\\DS_api")
    conn = sqlite3.connect('med_cabinet.sqlite3')
    c = conn.cursor()
    
    desc = []
    for i in lst:

        rows = c.execute("""SELECT * FROM Strain_info as S
                                JOIN Cannabinoids as C ON C.id=S.id
                                JOIN Terpenes as T ON T.id=S.id
                                WHERE S.id=""" + str(i)).fetchall()
        
        desc.append(rows)
    
    return desc
    
   
# test list to check if the function works   
lst = [45,32,23]
rows = queryDB(lst)
print(rows)