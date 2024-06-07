
import sqlite3
import pandas as pd

conn = sqlite3.connect('crypto_prices.db')

def get_price_changes(symbol):
    query = f"SELECT price, timestamp FROM prices WHERE symbol='{symbol}' ORDER BY timestamp DESC LIMIT 3"
    df = pd.read_sql_query(query, conn)
    df['price_change'] = df['price'].pct_change() * 100
    return df

# Örnek kullanım
symbols = ['BTCUSDT', 'ETHUSDT']
for symbol in symbols:
    price_changes = get_price_changes(symbol)
    print(price_changes)
