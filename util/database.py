import os
import sqlite3
from config import DATABASE_SYSTEM, DATABASE_USER, DATABASE_DIR

def initialize_db(db_path):
    os.makedirs(DATABASE_DIR, exist_ok=True)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    if db_path == DATABASE_SYSTEM:
        c.execute('''CREATE TABLE IF NOT EXISTS price_logs (symbol TEXT, price REAL, timestamp DATETIME)''')
        c.execute('''CREATE TABLE IF NOT EXISTS tracked_pairs (id INTEGER PRIMARY KEY AUTOINCREMENT, symbol TEXT NOT NULL UNIQUE)''')
        c.execute('''CREATE TABLE IF NOT EXISTS correlated_pairs (id INTEGER PRIMARY KEY AUTOINCREMENT, pair1 TEXT NOT NULL, pair2 TEXT NOT NULL)''')

    if db_path == DATABASE_USER:
        c.execute('''CREATE TABLE IF NOT EXISTS logs_cmd (id INTEGER PRIMARY KEY AUTOINCREMENT, command TEXT, usage_alltime INTEGER, usage_thisweek INTEGER, usage_lasttime DATETIME)''')

        commands = ['start', 'sub', 'help', 'info', 'bvol']
        for cmd in commands:
            c.execute('''INSERT INTO logs_cmd (command, usage_alltime, usage_thisweek, usage_lasttime) VALUES (?, ?, ?, ?)''', (cmd, 0, 0, None))

        c.execute('''CREATE TABLE IF NOT EXISTS users (number INTEGER PRIMARY KEY AUTOINCREMENT, id INTEGER NOT NULL UNIQUE)''')

    conn.commit()
    conn.close()
    print(f"Database and tables have been created in {db_path} path.")

if __name__ == '__main__':
    databases = [DATABASE_SYSTEM, DATABASE_USER]
    for db in databases:
        initialize_db(db)
