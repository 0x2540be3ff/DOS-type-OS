# terminal.py
import sys; import os; import time; import importlib; import string; import datetime; import re; import version; from lst_str import listToString; from blank import BLANK; from doesFileExist import doesFileExist; from file_write import WRITE;
os.system("cls")
time.sleep(0.5)
print("DOS_START")
time.sleep(0.5)
BLANK()
DOT = "▅▅▅▅▅"
print("Starting")
for y in DOT:
    time.sleep(1.5)
    sys.stdout.write(y)
    sys.stdout.flush()
time.sleep(2)
os.system("cls")
os.system("title DOS")
time.sleep(1)
inf = 1
USER1 = "users.txt"
print("NORMAL_MODE")
version.VER()
time.sleep(1)
BLANK()
print("Login 🡺")
USER = input("Username: ")
PASS = input("Password: ")
list_of_files = os.listdir()
user_ext = USER+".u5r"
if user_ext in list_of_files:
    file1 = open(user_ext, "r")
    verify = file1.read().splitlines()
    if PASS in verify:
        if PASS != USER:

            print("PASSWORD [ OK ]")
            time.sleep(1)
        else:
            print("Wrong password.")
            time.sleep(1)
            print("Shutting down...")
            time.sleep(0.5)
            quit(0)

    else:
        print("Wrong password.")
        time.sleep(1)
        print("Shutting down...")
        time.sleep(0.5)
        quit(0)

else:
    print("User does not exist.")
    time.sleep(1)
    print("Shutting down...")
    time.sleep(0.5)
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
        if os.path.getsize(USER1) == 0:
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
    elif COMMAND_PROMPT == "SHUTDOWN":
        print("Shutting down...")
        time.sleep(0.8)
        print("Goodbye.")
        time.sleep(1)
        os.system("cls")
        quit(0)
    elif COMMAND_PROMPT == "shutdown":
        print("Shutting down...")
        time.sleep(0.8)
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
    elif COMMAND_PROMPT == "RESTART /b":
        print("Restarting...")
        time.sleep(2)
        import boot_dos
        importlib.reload(boot_dos)
        quit(0)
    elif COMMAND_PROMPT == "restart /b":
        print("Restarting...")
        time.sleep(2)
        import boot_dos
        importlib.reload(boot_dos)
        quit(0)
    elif COMMAND_PROMPT == "RESTART /B":
        print("Restarting...")
        time.sleep(2)
        import boot_dos
        importlib.reload(boot_dos)
        quit(0)
    elif COMMAND_PROMPT == "restart /B":
        print("Restarting...")
        time.sleep(2)
        import boot_dos
        importlib.reload(boot_dos)
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
        F = open('help_US_nor.txt', 'r')
        HELP = F.read()
        print(HELP)
        F.close()
        continue
    elif COMMAND_PROMPT == "HELP":
        F = open('help_US_nor.txt', 'r')
        HELP = F.read()
        print(HELP)
        F.close()
        continue
    elif COMMAND_PROMPT == "DATE":
        TODAY = datetime.date.today()
        DATE = TODAY.strftime("%d/%m/%Y")
        print("Today's date is:",DATE)
    elif COMMAND_PROMPT == "date":
        TODAY = datetime.date.today()
        DATE = TODAY.strftime("%d/%m/%Y")
        print("Today's date is:",DATE)
        continue
    elif COMMAND_PROMPT == "TIME":
        NOW = datetime.datetime.now()
        TIME = NOW.strftime("%H:%M:%S")
        print("Current time is:",TIME,"(UTC+1)")
        continue
    elif COMMAND_PROMPT == "time":
        NOW = datetime.datetime.now()
        TIME = NOW.strftime("%H:%M:%S")
        print("Current time is:",TIME,"(UTC+1)")
        continue
    elif COMMAND_PROMPT == "VERSION":
        version.VER()
        continue
    elif COMMAND_PROMPT == "version":
        version.VER()
        continue
    elif "PRINT" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            print(y)
            continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
    elif "print" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            print(y)
            continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
    elif "FILE.READ" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            if doesFileExist(y):
                F = open(y, 'r')
                READ = F.read()
                print(READ)
                F.close()
                continue
            else:
                print("File does not exist.")
                continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
    elif "file.READ" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            if doesFileExist(y):
                F = open(y, 'r')
                READ = F.read()
                print(READ)
                F.close()
                continue
            else:
                print("File does not exist.")
                continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
    elif "FILE.read" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            if doesFileExist(y):
                F = open(y, 'r')
                READ = F.read()
                print(READ)
                F.close()
                continue
            else:
                print("File does not exist.")
                continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
    elif "file.read" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            if doesFileExist(y):
                F = open(y, 'r')
                READ = F.read()
                print(READ)
                F.close()
                continue
            else:
                print("File does not exist.")
                continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
    elif "FILE.OPEN" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            if doesFileExist(y):
                a = "notepad "+y
                #print(a)
                os.system(a)
            else:
                print("File does not exist.")
        else:
            print("Input Error: Perhaps you forgot } ?")
    elif "file.OPEN" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            if doesFileExist(y):
                a = "notepad "+y
                #print(a)
                os.system(a)
            else:
                print("File does not exist.")
        else:
            print("Input Error: Perhaps you forgot } ?")
    elif "FILE.open" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            if doesFileExist(y):
                a = "notepad "+y
                #print(a)
                os.system(a)
            else:
                print("File does not exist.")
        else:
            print("Input Error: Perhaps you forgot } ?")
    elif "file.open" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            if doesFileExist(y):
                a = "notepad "+y
                #print(a)
                os.system(a)
            else:
                print("File does not exist.")
        else:
            print("Input Error: Perhaps you forgot } ?")
    elif "FILE.WRITE" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            x = y.split(", ")
            z, zz = x
            file = str(z)
            text = str(zz)
            #print(file)
            print(text)
            WRITE(file, text)
            continue
        else:
            print("Input Error: Perhaps you forgot } ?")
    elif "file.WRITE" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            x = y.split(", ")
            z, zz = x
            file = str(z)
            text = str(zz)
            #print(file)
            print(text)
            WRITE(file, text)
            continue
        else:
            print("Input Error: Perhaps you forgot } ?")
    elif "FILE.write" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            x = y.split(", ")
            z, zz = x
            file = str(z)
            text = str(zz)
            #print(file)
            print(text)
            WRITE(file, text)
            continue
        else:
            print("Input Error: Perhaps you forgot } ?")
    elif "file.write" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            x = y.split(", ")
            z, zz = x
            file = str(z)
            text = str(zz)
            #print(file)
            print(text)
            WRITE(file, text)
            continue
        else:
            print("Input Error: Perhaps you forgot } ?")
    elif "FILE.CHEXT" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            x = y.split(", ")
            z, zz = x
            file = str(z)
            ext = str(zz)
            continue
        else:
            print("Input Error: Perhaps you forgot } ?")

    else:
        print("This command does not exist.")
        continue
