import telebot
from telebot import TeleBot

import config
from config import tgToken


bot = telebot.TeleBot(token=tgToken)

@bot.message_handler()
def wrong_words(message):
    text = message.text.lower()
    for word in config.wrong_words:
        if word in text:
            bot.delete_message(message.chat.id, message.message_id)


bot.infinity_polling()
