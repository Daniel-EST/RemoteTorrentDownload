import re
import time

import subprocess

import telegram as tg
from torrent_download import torrent_download

while True:
    # Reads last received message
    message = teste.read_message()
    
    # Checking if message corresponds to an action
    torrent_download(message)
    
    # Giving some time to API server
    time.sleep(2.5)
    
# TO DO: ADD MORE BOT ACTIONS
