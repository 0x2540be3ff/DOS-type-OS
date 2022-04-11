# terminal.py
import os; import time; import importlib; import string; import datetime; import re
os.system("cls")
time.sleep(0.5)
def BLANK():
    print("")
print("DOS_START")
time.sleep(0.5)
BLANK()
print("Starting...")
time.sleep(2)
os.system("cls")
os.system("title DOS")
time.sleep(1)
inf = 1
ver = "v 1.4.2"
USER1 = "users.txt"
def doesFileExists(filePathAndName):
    return os.path.exists(filePathAndName)

def listToString(x): 
    
    str1 = " " 
    return (str1.join(x))
        

def register_user(x, y):
  username_info = x
  password_info = y
  if doesFileExists(username_info):
    print("User already exists!")
  elif username_info != password_info:
    usr = username_info+".u5r"
    file=open(usr, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    file1=open("users.txt", "a+")
    file1.write(username_info+"\n")
    file1.close()
    print("User successfully registered!")
  else:
    print("Error: Password cannot be the same as username!")


print("TERMINAL_MODE")
print(ver)
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
        F = open('help_US.txt', 'r')
        HELP = F.read()
        print(HELP)
        F.close()
        continue
    elif COMMAND_PROMPT == "HELP":
        F = open('help_US.txt', 'r')
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
        print(ver)
        continue
    elif COMMAND_PROMPT == "version":
        print(ver)
        continue
    elif "START" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            x = "start "+y
            os.system(x)
            continue 
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
    elif "start" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            x = "start "+y
            os.system(x)
            continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
    elif "users.reg" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            x = y.split(", ")
            z, zz = x
            user = str(z)
            password = str(zz)
            #print(user)
            #print(password)
            register_user(user, password)
            continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
        continue
    elif "USERS.reg" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            x = y.split(", ")
            z, zz = x
            user = str(z)
            password = str(zz)
            print(user)
            print(password)
            register_user(user, password)
            continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
        continue
    elif "users.REG" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            x = y.split(", ")
            z, zz = x
            user = str(z)
            password = str(zz)
            print(user)
            print(password)
            register_user(user, password)
            continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
        continue
    elif "USERS.REG" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            x = y.split(", ")
            z, zz = x
            user = str(z)
            password = str(zz)
            print(user)
            print(password)
            register_user(user, password)
            continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
        continue
    elif COMMAND_PROMPT == "HOST.WHOAMI":
        os.system("whoami")
        continue
    elif COMMAND_PROMPT == "host.WHOAMI":
        os.system("whoami")
        continue
    elif COMMAND_PROMPT == "HOST.whoami":
        os.system("whoami")
        continue
    elif COMMAND_PROMPT == "host.whoami":
        os.system("whoami")
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
    elif "users.userinfo" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            if doesFileExists(y):
                F = open(y, 'r')
                INFO = F.read()
                print(INFO)
                F.close()
                continue
            else:
                print("User does not exist.")
                continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
    elif "USERS.userinfo" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            if doesFileExists(y):
                F = open(y, 'r')
                INFO = F.read()
                print(INFO)
                F.close()
                continue
            else:
                print("User does not exist.")
                continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
    elif "users.USERINFO" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            if doesFileExists(y):
                F = open(y, 'r')
                INFO = F.read()
                print(INFO)
                F.close()
                continue
            else:
                print("User does not exist.")
                continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
    elif "USERS.USERINFO" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            if doesFileExists(y):
                F = open(y, 'r')
                INFO = F.read()
                print(INFO)
                F.close()
                continue
            else:
                print("User does not exist.")
                continue
        else:
            print("Input Error: Perhaps you forgot } ?")
            continue
    elif "READ" in COMMAND_PROMPT:
        if COMMAND_PROMPT.endswith("}"):
            var = re.findall(r"\{(.*?)\}", COMMAND_PROMPT)
            y = listToString(var)
            if doesFileExists(y):
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
    else:
        print("This command does not exist.")
        continue

    
