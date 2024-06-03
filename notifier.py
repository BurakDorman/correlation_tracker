
import telegram

def send_notification(message):
    bot_token = '6959219060:AAG8nwCyk80bl_e3-mjNHiiPj2N0dcKNy2Y'
    chat_id = 'YOUR_CHAT_ID'
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

# Örnek kullanım
message = "BTCUSDT %5 yükseldi, ETHUSDT hareket bekleniyor."
send_notification(message)
