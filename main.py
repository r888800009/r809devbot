#!/usr/bin/env python
"""r809's bot"""
from importlib import import_module

import config as cf

__stop_callbacks__ = []

def load_api():
    """load chat api"""
    print("Loading apis")
    print(cf.config["Output"])

    connect_type = {
        "LineAPI": lambda: import_module("modules.line_api"),
        "TelegramAPI": lambda: import_module("modules.telegram_api")
        }

    for apis in cf.config["Output"]:
        print(apis)
        connect_type.get(apis)()

    import_module("modules.command")

def stop_handler(callback):
    "stop handler"
    __stop_callbacks__.append(callback)

def stop():
    "stop all modules"
    for callback in __stop_callbacks__:
        callback()

    print("Exit r809bot")

def main():
    """start programe"""
    print("Hello there, it's r809's bot")
    cf.load_config()
    load_api()
    print("done")

if __name__ == '__main__':
    main()
