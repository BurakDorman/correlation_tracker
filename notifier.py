import telegram
import asyncio
from config import BOT_TOKEN, CHAT_ID

async def send_notification(message):
    bot = telegram.Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

# Örnek kullanım
if __name__ == '__main__':
    message = "Bot başlatıldı!"
    asyncio.run(send_notification(message))