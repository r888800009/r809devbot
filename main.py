#!/usr/bin/env python
"""r809's bot"""
from importlib import import_module
import multiprocessing as mp
import time
import json
import config as cf
import init

__pool__ = {}

def load_config():
    """load configure file"""
    print("Loading Configure")
    # check config is exists
    config_file = ""
    try:
        config_file = open("config.json").read()
    except FileNotFoundError:
        init.create_new_confige()
        config_file = open("config.json").read()

    cf.CONFIG = json.loads(config_file)
    print("config dump")
    print(json.dumps(cf.CONFIG, indent=4))

def load_api():
    """load chat api"""
    print("Loading apis")
    print(cf.CONFIG["Output"])

    connect_type = {
        "LineAPI": lambda: import_module("modules.line_api"),
        "TelegramAPI": lambda: import_module("modules.telegram_api")
        }

    for apis in cf.CONFIG["Output"]:
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
        for apis in cf.CONFIG["Output"]:
            __pool__[apis].join()

def main():
    """start programe"""
    print("Hello there, it's r809's bot")
    load_config()
    load_api()
    stop_process()
    print("done")


main()
