import re
import time
import subprocess

def torrent_download(message, telegram_bot):
    """Checking if message is a torrent mirror link"""
    
    mirror = re.compile(r'/torrent (magnet:.*)')

    if mirror.search(message):
        try:
            # Open qbittorrent windows
            subprocess.Popen([r'C:\Users\Danie\\AppData\Roaming\BitTorrent\BitTorrent.exe', mirror.search(message).group(1)])
        except FileNotFoundError:
            pass
        
        try:
            # Open transmission linux
            subprocess.Popen([r'transmission-gtk', mirror.search(message).group(1)])
        except FileNotFoundError:
            pass
        
        tg_bot.send_message('Download started!')
        print('Download started!')
        
        ## TODO: Create my own torrent downloader so I don't need to use a subprocess
        
    time.sleep(1)
