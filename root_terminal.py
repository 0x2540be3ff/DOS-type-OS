# terminal.py
import os; import time; import importlib
os.system("cls")
time.sleep(1)
inf = 1
ver = "v 1.0"
USER = "users.txt"
print("ROOT_TERMINAL_MODE")
print(ver)
print("")
print("Type in RETURN /terminal or QUIT to leave.")
print("Please enter your password to access the terminal.")
time.sleep(.5)
PASSWORD = input("Password: ")
FILE_PASS = open("root_pass", "r")
FILE_READ = FILE_PASS.read()
if PASSWORD == FILE_READ:
    print("PASSWORD [ OK ]")
    FILE_PASS.close()
elif PASSWORD == "RETURN /terminal":
    import terminal
    quit(0)
elif PASSWORD == "QUIT":
    os.system("cls")
    quit(0)
else:
    quit(0)
time.sleep(1)
TER_USER = "ROOT"
print("USER :", TER_USER)
time.sleep(1)
os.system("cls")
time.sleep(1)
while inf < 2:
    COMMAND_PROMPT = input("root@terminal:~$ ")
    if COMMAND_PROMPT == "USERS /dir":
        if os.path.getsize(USER) == 0:
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
        if os.path.getsize(USER) == 0:
            print("No users exist.")
            continue
        else:
            USER_LIST = open("users.txt", "r")
            USER_DIR = USER_LIST.read()
            print(USER_DIR)
            USER_LIST.close()
        continue
    elif COMMAND_PROMPT == "users /dir":
        if os.path.getsize(USER) == 0:
            print("No users exist.")
            continue
        else:
            USER_LIST = open("users.txt", "r")
            USER_DIR = USER_LIST.read()
            print(USER_DIR)
            USER_LIST.close()
        continue
    elif COMMAND_PROMPT == "MAIN.GUI":
        import register
        quit(0)
    elif COMMAND_PROMPT == "main.GUI":
        import register
        quit(0)
    elif COMMAND_PROMPT == "MAIN.gui":
        import register
        quit(0)
    elif COMMAND_PROMPT == "main.gui":
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
    elif COMMAND_PROMPT == "ROOT.run /TERMINAL":
        print("Restarting...")
        time.sleep(2)
        import root_terminal
        quit(0)
    else:
        print("This command does not exist.")

    
