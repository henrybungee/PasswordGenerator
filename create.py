from firebase_admin import db
import os
import time
import getpass
import random

def create_pass(username, ref):
  os.system("clear")
  website = input("What website is this for?\n")

  if (website.strip() == ""):
    website = "Untitled Password" + str(random.randint(0, 1000))

  while True:
    password = getpass.getpass("What's the password for " +website+ ":\n")

    if (password.strip() == ""):
      print("Enter a password!")
    else:
      break

  os.system("clear")

  print("Password saved.")

  passData = {
    website.replace('.', '') : {
      "saved_password" : password
    }
  }
  
  time.sleep(2)
  os.system("clear")

  return passData