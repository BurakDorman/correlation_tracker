# This code block is required to send messages to the Telegram chat(s).
# It sends a message as the program starts, or when it catches a correlation.
import sys
import os
import asyncio
from telegram import Bot # type: ignore

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'util'))
from config import BOT_TOKEN, GROUP_ID

bot = Bot(token=BOT_TOKEN)

async def send_notification(message, chat_id=GROUP_ID):
    try:
        await asyncio.wait_for(bot.send_message(chat_id=chat_id, text=message), timeout=10)
    except asyncio.TimeoutError:
        print("Notification sending timed out.")
