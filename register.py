from tkinter import *
import os; import time

os.system("cls")

def doesFileExists(filePathAndName):
    return os.path.exists(filePathAndName)
  

  
def register_user():
  username_info = username.get()
  password_info = password.get()
  if doesFileExists(username_info):
    os.system("start error_user.vbs")
    
    
  else:
    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    file1=open("users.txt", "a+")
    file1.write(username_info+"\n")
    file1.close()
    os.system("start success.vbs")
  username_entry.delete(0, END)
  password_entry.delete(0, END)


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  screen1.resizable(False, False)
  screen1.configure(bg="#1a1c1b")
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
  register_btn1 = PhotoImage(file="register.png")
  Label(screen1, text = "Register", bg = "lightblue", width = "300", height = "2", font = ("Segoe UI Light", 13)).pack()
  Label(screen1, text = "Please enter details below:", fg="#ffffff", bg="#1a1c1b").pack()
  Label(screen1, text = "", fg="#ffffff", bg="#1a1c1b").pack()
  Label(screen1, text = "Username * ", fg="#ffffff", bg="#1a1c1b").pack()
  username_entry = Entry(screen1, textvariable = username, borderwidth=0)
  username_entry.pack()
  Label(screen1, text = "Password * ", fg="#ffffff", bg="#1a1c1b").pack()
  password_entry =  Entry(screen1, textvariable = password, borderwidth=0)
  password_entry.pack()
  Label(screen1, text = "", fg="#ffffff", bg="#1a1c1b").pack()
  Button(screen1, text = "Register", height = "36", width = "64", borderwidth=0, image=register_btn1, bg="#1a1c1b", command = register_user).pack()
  Label(screen1, text = "", fg="#ffffff", bg="#1a1c1b").pack()
  screen1.mainloop()

def TERMINAL_MODE():
  screen.destroy()
  import run_terminal
  
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("400x350")
  screen.resizable(False, False)
  screen.configure(bg="#1a1c1b")
  screen.title("Register v1.0")
  register_btn = PhotoImage(file="register.png")
  terminal_btn = PhotoImage(file="terminal.png")
  Label(text = "Welcome", bg = "lightblue", width = "300", height = "2", font = ("Segoe UI Light", 13)).pack()
  Label(text = "", bg="#1a1c1b").pack()
  Label(text = "Options 🡺", bg="#1a1c1b", fg="#ffffff", font = ("Segoe UI Light", 11)).pack()
  Label(text = "", bg="#1a1c1b").pack()
  Button(text = "Register",height = "36", width = "64", borderwidth=0, image=register_btn, bg="#1a1c1b",  command = register).pack()
  Label(screen, text = "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯", fg="#ffffff", bg="#1a1c1b").pack()
  Button(text = "Terminal",height = "36", width = "64", borderwidth=0, image=terminal_btn, bg="#1a1c1b",  command = TERMINAL_MODE).pack()
  Label(text = "", bg="#1a1c1b").pack()
  Label(text = "", bg="#1a1c1b").pack()
  Label(text = "", bg="#1a1c1b").pack()
  Label(text = "", bg="#1a1c1b").pack()
  Label(text = "© 2022", bg="#1a1c1b", fg="#ffffff").pack()
  Label(screen, text = "register.GUI                                                                                                      v 1.0 ", fg="#ffffff", bg="#444444").pack()
  Label(text = "                                                                                                                                     ", bg="#444444").pack()

  screen.mainloop()

main_screen()
  
