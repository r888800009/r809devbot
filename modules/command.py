"Handle command"

import threading
import main
import config as cf
import re

command_list = {'stop': lambda x: main.stop()}
user_command_list = {}

class Command(threading.Thread):
    "Handle command"
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True

    def run(self):
        "run"
        print("Start Command System")

        # wait for handle commands
        while self.running:
            if not self.running:
                return
            str1 = input("> ")
            command = str1.split()
            if not command:
                continue

            command_list.get(
                command[0],
                lambda cmd: print("Not found command \"%s\", \"help\"" % cmd))(command)

    def stop(self):
        "stop"
        print("stop command system")
        self.running = False

def load_commands():
    "load commands"
    # exit command
    command_list.update({'quit': lambda x: main.stop()})
    command_list.update({'exit': lambda x: main.stop()})
    command_list.update({'help': lambda x: help()})

    # load custom commands
    custom_commands = cf.config["Command"]["custom_commands"]
    for k in custom_commands.items():
        call = lambda x, y=k[1]: y
        add_user_command("/" + k[0], call)

    add_user_command("/help", user_help)

def add_command(keyword, callback):
    "Add command handler"
    command_list.update({keyword: callback})

def add_user_command(keyword, callback):
    "Add command handler for user input"
    print("Add user command \"" + keyword + "\"")
    user_command_list.update({keyword: callback})

def user_command_handler(command, reply_handler):
    "chatbot api call this to handler user commands"
    check = r'^/[a-zA-Z_]*'
    match = re.match(check, command)
    if not command or not match:
        return

    command_name = match.group(0)

    reply = user_command_list.get(
        command_name,
        lambda cmd, command_name=command_name:
        ("Not found command \"%s\", /help" % command_name))(command)

    reply_handler(reply)
    print(command)
    print(reply)

def user_help(command):
    result = "**Command list**\n"

    for k in user_command_list:
        result += k + '\n'

    return result

def help():
    for k in command_list:
        print(k)

def start_command_system():
    "run command system"
    __command__ = Command()
    __command__.start()

    @main.stop_handler
    def stop():
        "stop"
        __command__.stop()
