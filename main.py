import logging
import threading
from telegram import * # update
#from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler # CallbackContext
from util.config import BOT_TOKEN
from src.commands import *
from src.fetch_data import *

print('Starting DorAstBot...')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
stop_event = threading.Event()
def start_fetch_data():
    threading.Thread(target=fetch_data).start()

if __name__ == '__main__':
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler('start', cmd_start))
    application.add_handler(CommandHandler('help', cmd_help))
    application.add_handler(CommandHandler('info', cmd_info))
    application.add_handler(CommandHandler('add_pair', cmd_add_pair))

    start_fetch_data()

    application.run_polling(1.0)

    stop_event.set()

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [KeyboardButton("Add Pair"), KeyboardButton("Check Prices")]
    ]
    
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)
