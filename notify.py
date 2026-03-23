import requests
import sys

def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{8671753278:AAEiwDRESfK0k2bi-B6PdCGbROBqjXIzfzU}/sendMessage"
    payload = {
        'chat_id': 8671753278:AAEiwDRESfK0k2bi-B6PdCGbROBqjXIzfzU,
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, json=payload)
    return response.json()

if __name__ == "__main__":
    bot_token = sys.argv[1]
    chat_id = sys.argv[2]
    message = sys.argv[3]
    
    send_message(bot_token, chat_id, message)
