
import requests
import sqlite3
from datetime import datetime

# Veritabanı bağlantısı ve tablo oluşturma
conn = sqlite3.connect('crypto_prices.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS prices
             (symbol TEXT, price REAL, timestamp DATETIME)''')
conn.commit()

# Binance API'yi kullanarak fiyat verilerini çekme
def fetch_binance_prices(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    return response.json()

# Fiyat verilerini veritabanına kaydetme
def save_price(symbol, price):
    timestamp = datetime.now()
    c.execute("INSERT INTO prices (symbol, price, timestamp) VALUES (?, ?, ?)",
              (symbol, price, timestamp))
    conn.commit()

# Takip edilecek pariteleri veritabanından alma
def get_pairs():
    c.execute("SELECT symbol FROM pairs")
    return [row[0] for row in c.fetchall()]

# Örnek kullanım
symbols = get_pairs()  # Veritabanından pariteleri al
for symbol in symbols:
    price_data = fetch_binance_prices(symbol)
    save_price(price_data['symbol'], float(price_data['price']))
