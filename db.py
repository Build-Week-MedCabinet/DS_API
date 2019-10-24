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

        try:  # Connection for server instance
            # print(current_app.config['DATABASE'])  # DEBUG
            g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES,
            )
        except:  # Connection for local instance
            # print(current_app.config['LOCALDATABASE'])  # DEBUG
            g.db = sqlite3.connect(
                current_app.config['LOCALDATABASE'],
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

def query_database(lst):
    conn = get_db()
    c = conn.cursor()

    desc = []
    for i in lst:

        rows = c.execute("""SELECT * FROM Strain_info as S
                                JOIN Cannabinoids as C ON C.id=S.id
                                JOIN Terpenes as T ON T.id=S.id
                                WHERE S.id=""" + str(i)).fetchall()

        desc.append(rows)
    print(desc)
    return desc


# test list to check if the function works
# lst = [45,32,23]
# rows = queryDB(lst)
# print(rows)