import telegram as tg
import re
import subprocess

message = teste.read_message()

print(message)

torrent_regex = re.compile(r'/torrent .*')

if torrent_regex.search(message):
    print('achou')
    
# TO DO: CREATE A FUNCTION THAT START A BIT TORRENT APLICATION AND STARTS THE DOWNLOAD
