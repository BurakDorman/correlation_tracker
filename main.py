import threading
import asyncio
from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, CallbackContext
import sqlite3
import time
import fetch_data
from notifier import send_notification
from config import BOT_TOKEN

# add_pair komutunu işleyen fonksiyon
async def add_pair(update: Update, context: CallbackContext) -> None:
    pair = context.args[0]
    conn = sqlite3.connect('crypto_prices.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("INSERT INTO pairs (symbol) VALUES (?)", (pair,))
    conn.commit()
    conn.close()
    await update.message.reply_text(f"Pair {pair} added to the tracking list.")

# delete_pair komutunu işleyen fonksiyon
async def delete_pair(update: Update, context: CallbackContext) -> None:
    pair = context.args[0]
    conn = sqlite3.connect('crypto_prices.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("DELETE FROM pairs WHERE symbol=?", (pair,))
    conn.commit()
    conn.close()
    await update.message.reply_text(f"Pair {pair} removed from the tracking list.")

# add_correlated_pair komutunu işleyen fonksiyon
async def add_correlated_pair(update: Update, context: CallbackContext) -> None:
    pair1 = context.args[0]
    pair2 = context.args[1]
    fetch_data.add_correlated_pair(pair1, pair2)
    await update.message.reply_text(f"Correlated pairs added: {pair1}, {pair2}")

async def start_bot():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("add_pair", add_pair))
    application.add_handler(CommandHandler("delete_pair", delete_pair))
    application.add_handler(CommandHandler("add_correlated_pair", add_correlated_pair))
    await application.initialize()
    await application.start()
    await send_notification("Bot başlatıldı!")
    await application.run_polling()

def run_bot(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_bot())

def start_data_fetching():
    fetch_data.update_top_pairs()  # Program başlatıldığında en yüksek hacimli pariteleri güncelle
    while True:
        conn = sqlite3.connect('crypto_prices.db', check_same_thread=False)
        c = conn.cursor()
        fetch_data.c = c  # fetch_data modülünde kullanılan cursor'u güncelle
        symbols = fetch_data.get_pairs()  # Takip edilecek pariteleri güncelle
        for symbol in symbols:
            price_data = fetch_data.fetch_binance_prices(symbol)
            fetch_data.save_price(price_data['symbol'], float(price_data['price']))
        conn.close()
        time.sleep(30)  # Her 30 saniyede bir veri çek

if __name__ == '__main__':
    new_loop = asyncio.new_event_loop()
    bot_thread = threading.Thread(target=run_bot, args=(new_loop,))
    bot_thread.start()

    data_thread = threading.Thread(target=start_data_fetching)
    data_thread.start()

    bot_thread.join()
    data_thread.join()
