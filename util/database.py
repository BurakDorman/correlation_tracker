import sqlite3

def initialize_db():
    # Connect to the database.
    conn = sqlite3.connect('crypto_prices.db')
    c = conn.cursor()

    # Create 'prices' table.
    c.execute('''CREATE TABLE IF NOT EXISTS prices
                 (symbol TEXT, price REAL, timestamp DATETIME)''')

    # Create 'pairs' table.
    c.execute('''CREATE TABLE IF NOT EXISTS pairs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, symbol TEXT NOT NULL UNIQUE)''')

    # Create 'correlated_pairs' table.
    c.execute('''CREATE TABLE IF NOT EXISTS correlated_pairs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, pair1 TEXT NOT NULL, pair2 TEXT NOT NULL)''')

    conn.commit()
    conn.close()
    print("Veritabanı ve tablolar başarıyla oluşturuldu.")

if __name__ == '__main__':
    initialize_db()
