import json, sys, shutil

def createNewConfige():

    print("""config.json not found,
it seems like first time run r809's bot""")

    while True:
        print("Do You want to create a new one?[y/n]")
        choice = input().lower()
        if choice == 'y':
            shutil.copyfile("config.json.example", "config.json")
            return
        elif choice == 'n':
            print("Nope.")
            sys.exit()
            return


