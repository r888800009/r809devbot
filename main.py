#!/usr/bin/env python
from init import *

# check config is exists
config = ""
try:
    config = open("config.json").read()
except FileNotFoundError:
    createNewConfige()
    config = open("config.json").read()

data = json.loads(config)
print(data)
