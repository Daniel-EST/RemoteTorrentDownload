import re
import time
import subprocess

def torrent_download(message):
    """Checking if message is a torrent mirror link"""
    
    mirror = re.compile(r'/torrent (magnet:.*)')

    if mirror.search(message):
        # Open qbittorrent
        subprocess.Popen([r'C:\Users\Danie\\AppData\Roaming\BitTorrent\BitTorrent.exe', mirror.search(message).group(1)])
    
    time.sleep(1)
