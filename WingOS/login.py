import json
import time
from getpass import getpass
import username

with open("WingOS/credentials.json", "r+") as f:
    data = json.load(f)
    admin = data["admin"]
    adminpass = data["adminpass"]
    root= data["root"]
    rootpass=data["rootpass"]
    userpass=data["usrpass"]

authent=False
level=""

def auth():
    global authent
    global level
    username.nameauth()
    usrnme = username.user
    usrnme = str(usrnme)

    if usrnme == root:
        password = getpass(prompt="Password: ")
        password = str(password)

        if password == rootpass:
            level="root"
            authent=True
            return username, authent
        else:
            print("Username or password Incorrect")
    elif usrnme==admin:
        password = getpass(prompt="Password: ")
        password = str(password)

        if password == adminpass:
            authent=True
            return username, authent
        else:
            print("Username or password Incorrect")
    elif usrnme:
        password = getpass(prompt="Password: ")
        password = str(password)

        if password == userpass:
            level="low"
            authent=True
            return username, authent, level
        else:
            print("Username or password Incorrect")
    else:
        password = getpass(prompt="Password: ")
        password = str(password)
        print("Username or password Incorrect")

def change_password():
        changepass = str(input("Input new password: \n\n"))
        if len(changepass) >= 9:
            check = True
            while check:
                for x in range(len(changepass)):
                    symbol = [
                        "$", "£", "%", "^", "&", "*", "\"", "(", ")", "[", "]", "{", "}", "@", "!", "'", "#", "~", "<", ">", "`", "-", "_", "=", "+", ";", ":", ",", ".", "/", "?", "\\", "|", "¬", "¦", " "
                    ]
                    for b in range(len(symbol)):
                        if changepass[x] == symbol[b]:
                            print("Special Character Detected: %s" % symbol[b])
                            time.sleep(3)
                            exit(0)
                check = False
            data["adminpass"] = changepass
            with open("credentials.json", "r+") as f:
                f.truncate()
                json.dump(data, f)
            print("Password Changed!")
            time.sleep(5)

def change_username():
    changename = str(input("Input new username: \n\n"))
    if len(changename) >= 9:
        check = True
        while check:
            for x in range(len(changename)):
                symbol = [
                        "$", "£", "%", "^", "&", "*", "\"", "(", ")", "[", "]", "{", "}", "@", "!", "'", "#", "~", "<", ">", "`", "-", "_", "=", "+", ";", ":", ",", ".", "/", "?", "\\", "|", "¬", "¦", " "
                    ]
                for b in range(len(symbol)):
                    if changename[x] == symbol[b]:
                        print("Special Character Detected: %s" % symbol[b])
                        time.sleep(3)
                        exit(0)
            check = False
        data["admin"] = changename
        with open("credentials.json", "r+") as f:
            f.truncate()
            json.dump(data, f)
            print("Username Changed! Restarting in 5 seconds.")
            time.sleep(5)
            exit(0)