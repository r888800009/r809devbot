"Handle command"

import threading
import main

command_list = {'stop': lambda x: main.stop()}

class Command(threading.Thread):
    "Handle command"
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True

    def run(self):
        "run"
        print("Start Command System")

        # exit command
        command_list.update({'quit': lambda x: main.stop()})
        command_list.update({'exit': lambda x: main.stop()})

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
                lambda cmd: print("Not found command \"%s\"" % cmd))(command)

    def stop(self):
        "stop"
        print("stop command system")
        self.running = False

def add_command(keyword, callback):
    "Add command handler"
    command_list.update({keyword: callback})

def start_command_system():
    "run command system"
    __command__ = Command()
    __command__.start()

    @main.stop_handler
    def stop():
        "stop"
        __command__.stop()
