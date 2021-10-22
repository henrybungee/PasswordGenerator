import os
import time
import random

def generate():

  os.system("clear")
  print("Welcome to the Generator!")
  time.sleep(2)
  website = input("What website is this for?\n")

  if (not website):
    website = "Untitled Password" + str(random.randint(0, 1000))

  print("OK, generating a password for you.")
  time.sleep(2)

  characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@%^&*-="

  temp = random.sample(characters, 16)

  password = "".join(temp)
  os.system("clear")

  print("This is your password. Keep it safe and do not share it with anyone. Your password will be stored in your keychain for later use:\n" + password)

  passData = {
    website.replace('.', '') : {
      "saved_password" : password
    }
  }
  
  time.sleep(3)
  os.system("clear")

  return passData