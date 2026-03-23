import os
from telegram import Bot

TOKEN = '8671753278:AAEiwDRESfK0k2bi-B6PdCGbROBqjXIzfzU'
CHAT_ID = '8671753278'

bot = Bot(token=TOKEN)

def send_message(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    send_message("Сборка ядра началась!")

