# -*- coding: utf-8 -*-
import sys
import sqlite3
import csv
from flask import Flask, g

app = Flask(__name__)
SQLITE_DB_PATH = 'members.db'
SQLITE_DB_SCHEMA = 'create_db.sql'
MEMBER_CSV_PTAH = 'members.csv'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(SQLITE_DB_PATH)
        db.execute("PRAGMA foreign_keys = ON")
    return db

def creatDB():
    with open('.\create_db.sql', encoding='utf-8') as f:
        createDBSQL = f.read()

        with sqlite3.connect('members.db') as db:
            db.executescript(createDBSQL)

def writeData():
    with open('.\membersBig5.csv', newline='') as f:
        data = csv.DictReader(f)
        members = [(row['Name'], row['Group']) for row in data]

    with sqlite3.connect('members.db') as db:
        db.executemany('INSERT INTO members(name, group_name) VALUES(?, ?)',members)

def readData():
    with sqlite3.connect('members.db') as db:
        c = db.execute('SELECT * FROM members LIMIT 3')
    for row in c:
        print(row)
readData()
