import sqlite3
from telegram import Update
from telegram.ext import CallbackContext
import fetch_data

# Add a cryptocurrency to the tracking list.
async def add(update: Update, context: CallbackContext) -> None:
    if len(context.args) > 0:
        pair = context.args[0]
        conn = sqlite3.connect('crypto_prices.db', check_same_thread=False)
        c = conn.cursor()
        c.execute("INSERT INTO pairs (symbol) VALUES (?)", (pair,))
        conn.commit()
        conn.close()
        await update.message.reply_text(f"Pair {pair} added to the tracking list.")
    else:
        await update.message.reply_text("Please provide a pair to add.")

# Remove a cryptocurrency from the tracking list.
async def remove(update: Update, context: CallbackContext) -> None:
    if len(context.args) > 0:
        pair = context.args[0]
        conn = sqlite3.connect('crypto_prices.db', check_same_thread=False)
        c = conn.cursor()
        c.execute("DELETE FROM pairs WHERE symbol=?", (pair,))
        conn.commit()
        conn.close()
        await update.message.reply_text(f"Pair {pair} removed from the tracking list.")
    else:
        await update.message.reply_text("Please provide a pair to remove.")

# Register a/some correlated pair(s).
async def register_pair(update: Update, context: CallbackContext) -> None:
    if len(context.args) > 1:
        pair1 = context.args[0]
        pair2 = context.args[1]
        fetch_data.add_correlated_pair(pair1, pair2)
        await update.message.reply_text(f"Correlated pairs added: {pair1}, {pair2}")
    else:
        await update.message.reply_text("Please provide two pairs to add as correlated.")

# Delete a/some correlated pair(s).
async def delete_pair(update: Update, context: CallbackContext) -> None:
    if len(context.args) > 1:
        pair1 = context.args[0]
        pair2 = context.args[1]
        conn = sqlite3.connect('crypto_prices.db', check_same_thread=False)
        c = conn.cursor()
        c.execute("DELETE FROM correlated_pairs WHERE pair1=? AND pair2=?", (pair1, pair2))
        conn.commit()
        conn.close()
        await update.message.reply_text(f"Correlated pairs deleted: {pair1}, {pair2}")
    else:
        await update.message.reply_text("Please provide two pairs to delete.")

# Show the top 10 volume X/USDT pairs.
async def bvol(update: Update, context: CallbackContext) -> None:
    top_pairs = fetch_data.get_top_volume_pairs()
    await update.message.reply_text(f"Top 10 Volume Pairs: {', '.join(top_pairs)}")

# Show the tracking list.
async def tracklist(update: Update, context: CallbackContext) -> None:
    conn = sqlite3.connect('crypto_prices.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT symbol FROM pairs")
    pairs = [row[0] for row in c.fetchall()]
    await update.message.reply_text(f"Tracked Pairs: {', '.join(pairs)}")
    conn.close()

# Show the correlations list.
async def correlations(update: Update, context: CallbackContext) -> None:
    conn = sqlite3.connect('crypto_prices.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT pair1, pair2 FROM correlated_pairs")
    pairs = [f"{row[0]} - {row[1]}" for row in c.fetchall()]
    await update.message.reply_text(f"Correlated Pairs: {', '.join(pairs)}")
    conn.close()
