import sqlite3
connect=sqlite3.connect('urls.db',check_same_thread=False)
cursor=connect.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS urls(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               long_url TEXT NOT NULL,
               short_code TEXT UNIQUE
               )
               ''')
connect.commit()
