import re
import time

def torrent_download(mirror):
    """Checking if message is a torrent mirror link"""
    
    mirror = re.compile(r'/torrent *(.*)*')

    if mirror.search(message):
        # Open qbittorrent
        subprocess.Popen(['qbittorrent directory comes here', mirror.search(message).group(1)], shell=True)
    
    time.sleep(1)
    
    # TODO: add bittorrent application at subprocess