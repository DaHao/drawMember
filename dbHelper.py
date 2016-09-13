import sys
import sqlite3
import csv

with open('.\membersBig5.csv', newline='') as f:
    data = csv.DictReader(f)
    members = [(row['Name'], row['Group']) for row in data]

with open('.\create_db.sql',) as f:
    createDB = f.read

    with sqlite3.connect('members.db'):
        db.executescript(createDB)

