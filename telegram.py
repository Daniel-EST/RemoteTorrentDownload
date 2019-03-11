import requests
import json

class TelegramClass():
    def __init__(self, key, chat_id):
        """Initializing Telegram Class"""
        
        self.key = key
        self.chat_id = chat_id
        
    def send_message(self, text):
        """Sends a message for the current chat_id"""
        
        request = 'https://api.telegram.org/bot'
        request += self.key
        request += 'sendMessage?'
        
        request_params = {
            'chat_id': self.chat_id,
            'text': text,
            }
            
        requests.get(request, params=request_params)
        
    def send_image(self, image, caption):
        """Sends an image for the current chat_id"""
        
        ## TODO: send_image function properly
        
    def read_message(self):
        """Read the last message received by the bot"""
        
        request = 'https://api.telegram.org/bot'
        request += self.key
        request += 'getUpdates?'
        
        request_params = {
            'offset': -1,
            'limit': 1,
            'allowed_updates': 'message',
            }
            
        req = requests.get(request, params=request_params)
        
        # TO DO: CREATE A PROPER FUNCTION THAT SKIPS IF THE LAST MESSAGE
        # WAS ALREADY READ
        
        if req.status_code==200:
            json_data = req.json()
            received_message = json_data['result'][0]['message']['text']
            
            return received_message