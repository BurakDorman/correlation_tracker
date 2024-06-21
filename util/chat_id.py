import requests
from config import BOT_TOKEN

# With getUpdates method, all messages that the bot received.
response = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates')
updates = response.json()

# Look around the updates and find the ID.
if updates['ok']:
    for result in updates['result']:
        if 'message' in result:
            print('Chat ID:', result['message']['chat']['id'])
        else:
            print('No message key in result:', result)
else:
    print('Hata:', updates)

# Chat ID from the first update.
if updates['result']:
    if 'message' in updates['result'][0]:
        chat_id = updates['result'][0]['message']['chat']['id']
        print('Chat ID:', chat_id)
    else:
        print('First result has no message key:', updates['result'][0])
else:
    print('No chat ID.')
