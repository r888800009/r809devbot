"""load config file"""
import json
import sys
import shutil

config = {} # pylint: disable=C0103

def create_new_confige():
    """creat config file"""
    print("""config.json not found,
it seems like first time run r809's bot""")

    while True:
        print("Do You want to create a new one?[y/n]")
        choice = input().lower()
        if choice == 'y':
            shutil.copyfile("config.json.example", "config.json")
            return
        print("Nope.")
        sys.exit()
        return

def load_config():
    """load configure file"""
    print("Loading Configure")
    # check config is exists
    config_file = ""
    try:
        config_file = open("config.json").read()
    except FileNotFoundError:
        create_new_confige()
        config_file = open("config.json").read()

    config = json.loads(config_file) # pylint: disable=W0621
    print("config dump")
    print(json.dumps(config, indent=4))
