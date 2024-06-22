import os
import sqlite3
from config import SYSTEM_DATABASE, USER_DATABASE, DATABASE_DIR

def add_column_to_table(database_name: str, table_name: str, column_name: str):
    conn = sqlite3.connect(database_name, check_same_thread=False)
    c = conn.cursor()

    try:
        c.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} REAL")
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Error adding column {column_name}: {e}")

    conn.close()

def initialize_db(db_path):
    os.makedirs(DATABASE_DIR, exist_ok=True)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    if db_path == SYSTEM_DATABASE:
        c.execute('''CREATE TABLE IF NOT EXISTS logs (timestamp DATETIME)''')
        c.execute('''CREATE TABLE IF NOT EXISTS pairs (id INTEGER PRIMARY KEY AUTOINCREMENT, symbol TEXT NOT NULL UNIQUE, correlation INTEGER NOT NULL, coingecko TEXT)''')

        pairs = ['STX', 'BB', '1000SATS', 'ORDI'] # , 'ENA', 'LDO', 'ETHFI'
        for pair in pairs:
            add_column_to_table(SYSTEM_DATABASE, "logs", pair)

    if db_path == USER_DATABASE:
        c.execute('''CREATE TABLE IF NOT EXISTS users (num INTEGER PRIMARY KEY AUTOINCREMENT, id INTEGER NOT NULL UNIQUE, rank INTEGER CHECK(rank IN (0, 1, 2)))''')
        c.execute('''CREATE TABLE IF NOT EXISTS statistics (id INTEGER PRIMARY KEY AUTOINCREMENT, command TEXT, usage_alltime INTEGER, usage_thisweek INTEGER, usage_lasttime DATETIME)''')

        commands = ['start', 'sub', 'help', 'info', 'bvol']
        for cmd in commands:
            c.execute('''INSERT INTO statistics (command, usage_alltime, usage_thisweek, usage_lasttime) VALUES (?, ?, ?, ?)''', (cmd, 0, 0, None))
    
    conn.commit()
    conn.close()
    print(f"Database and tables have been created in {db_path} path.")

if __name__ == '__main__':
    databases = [SYSTEM_DATABASE, USER_DATABASE]
    for db in databases:
        initialize_db(db)
