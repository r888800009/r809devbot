"""modules for telegram API"""
import re
import jieba
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import config as cf
import main
import modules.command as cmd

print("Start telegram API")

updater = Updater(cf.config["TelegramAPI"]["Token"])
dispatcher = updater.dispatcher

def echo(bot, update):
    print(update.message)
    seg_list = jieba.cut(update.message.text)
    # bot.send_message(chat_id=update.message.chat_id, text=", ".join(seg_list))

def telegram_command(bot, update):
    message = update.message.text
    print(update)
    regex = re.compile('^/[a-zA-Z_]+@' + bot.username + r'($|\s)')
    if '@' in message and not re.match(regex, message):
        return

    def reply(msg):
        bot.send_message(chat_id=update.message.chat_id, text=msg)

    cmd.user_command_handler(message, reply)

echo_handler = MessageHandler(Filters.text, echo)
command_handler = MessageHandler(Filters.command, telegram_command)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(command_handler)

updater.start_polling()

@main.stop_handler
def stop():
    "stop"
    updater.stop()

chat_id1 = " "
def command(args):
    "consle commands"
    global chat_id1
    print(args)
    if len(args) >= 3:
        if args[1] == "say":
            updater.bot.send_message(chat_id=chat_id1, text=" ".join(args[2:]))
        elif args[1] == "set_say_chat_id":
            chat_id1 = args[2]

cmd.add_command("tg", command)
cmd.add_command("telegram", command)
