"""init"""
import sys
import shutil

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
