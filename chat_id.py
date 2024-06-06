import requests

# Bot token'ınızı buraya ekleyin
BOT_TOKEN = '6959219060:AAG8nwCyk80bl_e3-mjNHiiPj2N0dcKNy2Y'

# getUpdates metodu ile botun aldığı mesajları alın
response = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates')
updates = response.json()

# Güncellemeleri inceleyin ve chat ID'yi bulun
if updates['ok']:
    for result in updates['result']:
        print('Chat ID:', result['message']['chat']['id'])
else:
    print('Hata:', updates)

# İlk güncellemeden gelen chat ID'yi alabilirsiniz
if updates['result']:
    chat_id = updates['result'][0]['message']['chat']['id']
    print('Chat ID:', chat_id)
else:
    print('Chat ID bulunamadı.')
