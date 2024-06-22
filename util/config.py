import os

BOT_TOKEN = 'BOT_TOKEN'
GROUP_ID = 'CHAT_ID'
ADMIN_ID = 'ADMIN_ID' # {'id': 7475046663, 'is_bot': False, 'first_name': 'Burak', 'last_name': 'Dorman', 'username': 'burakdorman', 'language_code': 'en'}
DATABASE_DIR = os.path.join(os.path.dirname(__file__), '../database/')
SYSTEM_DATABASE= os.path.join(DATABASE_DIR, 'system.db')
USER_DATABASE = os.path.join(DATABASE_DIR, 'user.db')
LANGUAGE_FILE = os.path.join(DATABASE_DIR, 'strings.json')

DEBUG = True
