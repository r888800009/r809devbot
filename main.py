#!/usr/bin/env python
import pprint
from init import *

# check config is exists
config = ""
try:
    config = open("config.json").read()
except FileNotFoundError:
    createNewConfige()
    config = open("config.json").read()

data = json.loads(config)
print(json.dumps(data, indent =4))
