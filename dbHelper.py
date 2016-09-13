# -*- coding: utf-8 -*-
import sys
import sqlite3
import csv

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
