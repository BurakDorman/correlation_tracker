# This code block is required to send messages to the Telegram chat(s).
# It sends a message as the program starts, or when it catches a correlation.
import telegram
import asyncio
from config import BOT_TOKEN, CHAT_ID

async def send_notification(message):
    bot = telegram.Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == '__main__':
    message = "Bot initialized."
    asyncio.run(send_notification(message))
