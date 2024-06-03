
import threading
import fetch_data
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import sqlite3
import time

# Veritabanı bağlantısı ve tablo oluşturma
conn = sqlite3.connect('crypto_prices.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS pairs
             (id INTEGER PRIMARY KEY AUTOINCREMENT, symbol TEXT NOT NULL)''')
conn.commit()

# add_pair komutunu işleyen fonksiyon
def add_pair(update: Update, context: CallbackContext) -> None:
    pair = context.args[0]
    c.execute("INSERT INTO pairs (symbol) VALUES (?)", (pair,))
    conn.commit()
    update.message.reply_text(f"Pair {pair} added to the tracking list.")

def start_bot():
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("add_pair", add_pair))
    updater.start_polling()
    updater.idle()

def start_data_fetching():
    while True:
        fetch_data.symbols = fetch_data.get_pairs()  # Takip edilecek pariteleri güncelle
        for symbol in fetch_data.symbols:
            price_data = fetch_data.fetch_binance_prices(symbol)
            fetch_data.save_price(price_data['symbol'], float(price_data['price']))
        time.sleep(60)  # Her 60 saniyede bir veri çek

if __name__ == '__main__':
    threading.Thread(target=start_bot).start()
    threading.Thread(target=start_data_fetching).start()
