# root.py
import os; import time; import importlib; import string; import datetime; import re; import version; from lst_str import listToString; from blank import BLANK; from doesFileExist import doesFileExist;
os.system("cls")
time.sleep(1)
inf = 1
def register_user(x, y):
  username_info = x
  password_info = y
  if doesFileExist(username_info):
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
USER1 = "users.txt"
print("ROOT_MODE")
version.VER()
BLANK()
print("Type in RETURN /terminal or QUIT to leave.")
BLANK()
print("Please enter your password to access the terminal.")
time.sleep(0.5)
PASSWORD = input("Password: ")
FILE_PASS = open("root_pass", "r")
FILE_READ = FILE_PASS.read()
if PASSWORD == FILE_READ:
    print("PASSWORD [ OK ]")
    FILE_PASS.close()
elif PASSWORD == "RETURN /terminal":
    #importlib.reload(terminal)
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
TER = "root@terminal:~$ "
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
    elif COMMAND_PROMPT == "USERS.REG /GUI":
        os.system("cls")
        os.system("py register.py")
        quit(0)
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
        version.VER()
        continue
    elif COMMAND_PROMPT == "version":
        version.VER()
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
            if doesFileExist(y):
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
            if doesFileExist(y):
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
            if doesFileExist(y):
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
            if doesFileExist(y):
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

    
