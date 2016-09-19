import csv
import sqlite3
from flask import Flask, g, render_template, request
import random

app = Flask(__name__)
SQLITE_DB_PATH = 'members.db'
SQLITE_DB_SCHEMEA = 'create_db.sql'
MEMBER_CSV_PATH = 'membersBig5.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw', methods=['POST'])
def draw():
    db = get_db()

    group_name = request.form.get('group_name', 'ALL')
    valid_members_sql = 'SELECT id FROM members '
    if group_name == 'ALL':
        cursor = db.execute(valid_members_sql)
    else:
        valid_members_sql += 'WHERE group_name = ?'
        cursor = db.execute(valid_members_sql, (group_name, ))
    valid_member_ids = [ row[0] for row in cursor ]

    if not valid_member_ids:
        err_msg = "<p>No members in gorup '%s'</p>" % group_name
        return err_msg, 404

    lucky_member_id = random.choice(valid_member_ids)

    member_name, member_group_name = db.execute('SELECT name, group_name FROM members WHERE id = ?', (lucky_member_id, )).fetchone()

    return render_template('draw.html', name=member_name, group=member_group_name, )

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(SQLITE_DB_PATH)
        db.execute('PRAGMA foreign_keys = ON')
    return db

@app.teardown_appcontext
def close_connection(excetion):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)
