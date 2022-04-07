# terminal.py
import os; import time; import importlib; import string
os.system("cls")
time.sleep(1)
inf = 1
ver = "v 1.0"
USER1 = "users.txt"
print("TERMINAL_MODE")
print(ver)
time.sleep(1)
print("")
print("Login 🡺")
USER = input("Username: ")
PASS = input("Password: ")
list_of_files = os.listdir()

if USER in list_of_files:
    file1 = open(USER, "r")
    verify = file1.read().splitlines()
    if PASS in verify:
        print("PASSWORD [ OK ]")
        time.sleep(1)
    else:
        print("Wrong password.")
        time.sleep(1)
        print("Quiting...")
        time.sleep(.5)
        quit(0)

else:
    print("User does not exist.")
    time.sleep(1)
    print("Quiting...")
    time.sleep(.5)
    quit(0)
TER_USER = USER
LOW_USER = TER_USER.lower()
STR_USER = LOW_USER.replace(" ", "_")
print("USER :", TER_USER)
TER = STR_USER+"@terminal:~$ "
time.sleep(1)
os.system("cls")
time.sleep(1)
while inf < 2:
    COMMAND_PROMPT = input(TER)
    if COMMAND_PROMPT == "USERS /dir":
        if os.path.getsize(USER1) == 0:
            print("No users exist.")
            continue
        else:
            USER_LIST = open("users.txt", "r")
            USER_DIR = USER_LIST.read()
            print(USER_DIR)
            USER_LIST.close()
        continue
    elif COMMAND_PROMPT == "USERS /DIR":
        if os.path.getsize(USER) == 0:
            print("No users exist.")
            continue
        else:
            USER_LIST = open("users.txt", "r")
            USER_DIR = USER_LIST.read()
            print(USER_DIR)
            USER_LIST.close()
        continue
    elif COMMAND_PROMPT == "users /DIR":
        if os.path.getsize(USER1) == 0:
            print("No users exist.")
            continue
        else:
            USER_LIST = open("users.txt", "r")
            USER_DIR = USER_LIST.read()
            print(USER_DIR)
            USER_LIST.close()
        continue
    elif COMMAND_PROMPT == "users /dir":
        if os.path.getsize(USER1) == 0:
            print("No users exist.")
            continue
        else:
            USER_LIST = open("users.txt", "r")
            USER_DIR = USER_LIST.read()
            print(USER_DIR)
            USER_LIST.close()
        continue
    elif COMMAND_PROMPT == "USERS.REG /GUI":
        import register
        quit(0)
    elif COMMAND_PROMPT == "USERS.REG /gui":
        import register
        quit(0)
    elif COMMAND_PROMPT == "USERS.reg /GUI":
        import register
        quit(0)
    elif COMMAND_PROMPT == "users.reg /gui":
        import register
        quit(0)
    elif COMMAND_PROMPT == "users.reg /GUI":
        import register
        quit(0)
    elif COMMAND_PROMPT == "USERS.reg /gui":
        import register
        quit(0)
    elif COMMAND_PROMPT == "users.REG /GUI":
        import register
        quit(0)
    elif COMMAND_PROMPT == "users.REG /gui":
        import register
        quit(0)
    elif COMMAND_PROMPT == "QUIT":
        print("Quiting...")
        time.sleep(0.5)
        print("Goodbye.")
        time.sleep(1)
        os.system("cls")
        quit(0)
    elif COMMAND_PROMPT == "quit":
        print("Quiting...")
        time.sleep(0.5)
        print("Goodbye.")
        time.sleep(1)
        os.system("cls")
        quit(0)
    elif COMMAND_PROMPT == "CLEAR":
        os.system("cls")
        continue
    elif COMMAND_PROMPT == "clear":
        os.system("cls")
        continue
    elif COMMAND_PROMPT == "RESTART":
        print("Restarting...")
        time.sleep(2)
        import terminal
        importlib.reload(terminal)
        quit(0)
    elif COMMAND_PROMPT == "restart":
        print("Restarting...")
        time.sleep(2)
        import terminal
        importlib.reload(terminal)
        quit(0)
    elif COMMAND_PROMPT == "logoff":
        print("Logging off...")
        time.sleep(2)
        import terminal
        importlib.reload(terminal)
        quit(0)
    elif COMMAND_PROMPT == "LOGOFF":
        print("Logging off...")
        time.sleep(2)
        import terminal
        importlib.reload(terminal)
        quit(0)
    elif COMMAND_PROMPT == "IMPORT THIS":
        import this
        continue
    elif COMMAND_PROMPT == "import this":
        import this
        continue
    elif COMMAND_PROMPT == "IMPORT this":
        import this
        continue
    elif COMMAND_PROMPT == "import THIS":
        import this
        continue
    elif COMMAND_PROMPT == "ROOT.run /TERMINAL":
        print("Restarting...")
        time.sleep(2)
        import root_terminal
        quit(0)
    elif COMMAND_PROMPT == "help":
        F = open('help.txt', 'r')
        HELP = F.read()
        print(HELP)
        F.close()
        continue
    else:
        print("This command does not exist.")
        continue
