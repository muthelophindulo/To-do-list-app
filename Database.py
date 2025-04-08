import sqlite3 as sq
from todo import app

connection = sq.connect("data.db")

cur = connection.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS todo(
               id INTEGER PRIMARY KEY AUTOIMCREMENT,
               item TEXT NOT NULL)''')
