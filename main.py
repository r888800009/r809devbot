#!/usr/bin/env python
from importlib import import_module
import pprint
import config as cf
import multiprocessing as mp
import time
from init import *

print("Hello there, it's r809's bot")
print("/*------------------------*/")
# check config is exists
configFile = ""
try:
    configFile = open("config.json").read()
except FileNotFoundError:
    createNewConfige()
    configFile = open("config.json").read()

cf.config = json.loads(configFile)
print("config dump")
print(json.dumps(cf.config, indent = 4))


print("/*------------------------*/")
print("Loading apis")
print(cf.config["Output"])

connectType = {
        "LineAPI": lambda : import_module("modules.line")
        }

process = {}
for apis in cf.config["Output"]:
    print(apis)
    process[apis] = mp.Process(target = connectType.get(apis))
    process[apis].start()

import_module("modules.command")

try:
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    for apis in cf.config["Output"]:
        process[apis].join()

print("done")
