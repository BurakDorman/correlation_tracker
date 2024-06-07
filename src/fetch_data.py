import requests
import sqlite3
from datetime import datetime

# Veritabanı bağlantısı ve tablo oluşturma
conn = sqlite3.connect('crypto_prices.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS prices
             (symbol TEXT, price REAL, timestamp DATETIME)''')
c.execute('''CREATE TABLE IF NOT EXISTS pairs
             (id INTEGER PRIMARY KEY AUTOINCREMENT, symbol TEXT NOT NULL)''')
c.execute('''CREATE TABLE IF NOT EXISTS correlated_pairs
             (id INTEGER PRIMARY KEY AUTOINCREMENT, pair1 TEXT NOT NULL, pair2 TEXT NOT NULL)''')
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
    pairs = [row[0] for row in c.fetchall()]
    print("Kontrol edilen pariteler:", pairs)  # Kontrol edilen pariteleri yazdır
    return pairs

# Binance'deki en yüksek hacimli 10 coin/USDT paritesini çekme ve veritabanına ekleme
def update_top_pairs():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data = response.json()

    # Hacime göre sıralama
    top_pairs = sorted(data, key=lambda x: float(x['quoteVolume']), reverse=True)[:10]
    top_usdt_pairs = [pair['symbol'] for pair in top_pairs if pair['symbol'].endswith('USDT')]

    c.executemany("INSERT OR IGNORE INTO pairs (symbol) VALUES (?)", [(pair,) for pair in top_usdt_pairs])
    conn.commit()
    print("Güncellenen en yüksek hacimli pariteler:", top_usdt_pairs)

# Korelasyonlu pariteleri veritabanına ekleme
def add_correlated_pair(pair1, pair2):
    c.execute("INSERT INTO correlated_pairs (pair1, pair2) VALUES (?, ?)", (pair1, pair2))
    conn.commit()
    print(f"Korelasyonlu pariteler eklendi: {pair1}, {pair2}")

# Örnek kullanım
if __name__ == '__main__':
    update_top_pairs()
    # Örnek korelasyonlu pariteler
    add_correlated_pair('LOKAUSDT', 'VOXELUSDT')
    add_correlated_pair('LOKAUSDT', 'PIXELUSDT')
    add_correlated_pair('SFPUSDT', 'C98USDT')
    add_correlated_pair('SFPUSDT', 'TWTUSDT')
    add_correlated_pair('BBUSDT', 'ENAUSDT')
    add_correlated_pair('NOTUSDT', 'TONUSDT')
