#!/usr/bin/env python
from importlib import import_module
import pprint
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

config = json.loads(configFile)
print("config dump")
print(json.dumps(config, indent = 4))


print("/*------------------------*/")
print("Loading apis")
print(config["Output"])

connectType = {
        "LineAPI": lambda : import_module("modules.line")
        }
for apis in config["Output"]:
    print(apis)
    connectType.get(apis)()
