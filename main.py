#!/usr/bin/env python
"""r809's bot"""
from importlib import import_module
import multiprocessing as mp
import time

import config as cf

__pool__ = {}

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
        __pool__[apis] = mp.Process(target=connect_type.get(apis))
        __pool__[apis].start()

    import_module("modules.command")

def stop_process():
    """wait to stop Process"""
    try:
        while 1:
            time.sleep(1)
    except KeyboardInterrupt:
        for apis in cf.config["Output"]:
            __pool__[apis].join()

def main():
    """start programe"""
    print("Hello there, it's r809's bot")
    cf.load_config()
    load_api()
    stop_process()
    print("done")


main()
