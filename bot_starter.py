import re
import time

import telegram as tg
from torrent_download import torrent_download

# Load API keys
with open('api_keys') as text_obj:
    telegram_key = text_obj.readline().strip() + '/'
    telegram_chat_id = text_obj.readline().strip()
    
tg_bot = tg.TelegramClass(telegram_key, telegram_chat_id)

temp = ''

print('Programm started!')

try:
    while True:
        # Reads last received message
        message = tg_bot.read_message()
    
        if message!=temp:
            # Checking if message corresponds to an action
            torrent_download(message)
    
        temp = message
    
        # Giving some time to API server
        time.sleep(3)
except KeyboardInterrupt:
    print('Programm ended')
    
## TODO: ADD MORE BOT ACTIONS
