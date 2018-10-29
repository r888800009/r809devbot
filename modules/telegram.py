#!/usr/bin/env python
from telegram.ext import Updater, CommandHandler
import config as cf
print("Start telegram API")

updater = Updater(cf.config["TelegramAPI"]["Token"])
dispatcher = updater.dispatcher

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
