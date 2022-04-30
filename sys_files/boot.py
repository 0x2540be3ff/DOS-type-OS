# boot.py
import os; import time; import sys;
os.system("cls")
os.system("title DOS_BOOT")
time.sleep(1)
inf = 2
if "idlelib.run" in sys.modules:
    print("ERROR 0x1")
    sys.exit("Program not compatible with IDLE.")
else:
    print("", end = "")
print("""
_______________________________
  _____   ____   _____ 
 |  __ \ / __ \ / ____|
 | |  | | |  | | (___  
 | |  | | |  | |\___ \ 
 | |__| | |__| |____) |
 |_____/ \____/|_____/ v 1.4.2
_______________________________
""")
time.sleep(2)
print("")
print("Select boot option: ")
print("→ Normal boot | 1")
print("→ Shutdown | 2")
time.sleep(1)
print("")
x = int(input(">> "))
if x == 1:
  import terminal
  quit(0)
elif x == 2:
  print("Goodbye!")
  time.sleep(1.5)
  os.system("cls")
  quit(0)
else:
  print("This option does not exist.")
  time.sleep(1)
  print("Shutting down...")
  time.sleep(1.5)
  os.system("cls")
  quit(0)



  


