import sqlite3

# Veritabanı bağlantısı ve tablo oluşturma
conn = sqlite3.connect('crypto_prices.db')
c = conn.cursor()

# prices tablosunu oluşturma
c.execute('''
CREATE TABLE IF NOT EXISTS prices (
    symbol TEXT,
    price REAL,
    timestamp DATETIME
)
''')

# pairs tablosunu oluşturma
c.execute('''
CREATE TABLE IF NOT EXISTS pairs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Tablolar oluşturuldu.")
