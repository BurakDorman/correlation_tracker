import requests # type: ignore
from config import BOT_TOKEN

# With getUpdates method, all messages that the bot received.
response = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates')
updates = response.json()

# Look around the updates and find the ID.
if updates['ok']:
    for result in updates['result']:
        print('Chat ID:', result['message']['chat']['id'])
else:
    print('Hata:', updates)

# Chat ID from the first update.
if updates['result']:
    chat_id = updates['result'][0]['message']['chat']['id']
    print('Chat ID:', chat_id)
else:
    print('No chat ID.')
