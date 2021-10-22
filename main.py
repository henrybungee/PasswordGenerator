import firebase_admin
from firebase_admin import db
import time
import os
import getpass 

#import other scripts
import generate
import clear
import list
import view_pass as view
import editpass as edit
import create
import remove

if not firebase_admin._apps:
  cred_object = firebase_admin.credentials.Certificate('ENTER_SECRET_JSON_FILE_HERE')
  firebase_admin = firebase_admin.initialize_app(cred_object, {'databaseURL': 'ENTER_URL_HERE'})


ref = db.reference("/")

#--------------------------COMMANDS---------------------------------


def logged_in(username):
  print("What do you want to do?")
  while True:
    command = input("> ").lower().strip()
    args = command.split()

    if (command.startswith("generate")):
      
      userRef = db.reference(username + "/passwords/")
      
      userRef.update(generate.generate())
    elif (command.startswith("list")):

      listRef = db.reference(username + "/passwords/")
      list.list_passwords(listRef, username)

    elif (command.startswith("view")):
      if (not args):
        return print("ERROR: Takes 1 argument!")
      else:
        view.view_password(ref, username, args)

    elif (command.startswith("remove")):
      if (not args):
        return print("ERROR: Takes 1 argument!")
      else:
        remove.remove_password(username, ref, args)

    elif (command.startswith("clear")):
      clear.clear()

    elif (command.startswith("edit")):
        edit.edit_pass(username, args)

    elif (command.startswith("create")):

      userRef = db.reference(username + "/passwords/")
      userRef.update(create.create_pass(username, ref))

    elif (command.startswith("logout")):
      print("Logging out...")
      time.sleep(2)
      os.system("clear")
      login_or_create()

    elif (command.startswith("help")):
      f = open('help.txt', 'r')
      file_contents = f.read()
      print(file_contents)


    else:
      print("ERROR: Invalid command: \"" +command + "\"")
          

#----------------------------------------------------------------------


def login_func():
  while True:
    inUser = input("Enter a username:\n")
    inPass = getpass.getpass("Enter a password:\n")

    userPass = db.reference(inUser + "/" + "password")

    if (inPass == userPass.get()):
      os.system("clear")
      print("Logging you in...")
      time.sleep(2)
      print("Welcome, " +inUser)
      logged_in(inUser)
      break
    else:
      print("Incorrect username or password!")
      time.sleep(1)
      os.system("clear")

def create_account():
  username = input("Enter a username:\n")
  password = getpass.getpass("Enter a password:\n")

  data = {
    username : {
      "password" : password
    }
  }

  try:
    ref.update(data)
    print("Account successfully created")
    time.sleep(1)
    os.system("clear")
    login_func()
  except:
    print("There was an error making your account!")

def login_or_create():
  while True:
    print("Welcome to QuickPass!\nPlease login or make an account accordingly to get started.\n")
    login = input("Login or create account (l/c)").lower()

    if login.startswith("l"):
      login_func()
      break
    elif login.startswith("c"):
      create_account()
      break

login_or_create()