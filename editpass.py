from firebase_admin import db
import os
import getpass

def change_password_logic(x, username, confirmation):
  while True:
    confirmInput = getpass.getpass("Enter password to change password:\n")

    if (confirmInput == confirmation):    

      passWordRef = db.reference(username + "/passwords/" + x)

      newPassWord = getpass.getpass("Enter your new password:\n")

      if (newPassWord.strip() != ""):
        passWordRef.update({"saved_password" : newPassWord})
        print("Your new password for " +x+ " has been updated!")
        break

      else:
        print("Enter a password!")
      
    else:
      print("Wrong password!")
  
def edit_pass(username, args):

  os.system("clear")

  passRef = db.reference(username + "/passwords/")
  passWords = passRef.get()

  i = 0

  try:
    for x in passWords:
      if (i == int(args[1]) - 1):

        confirmation = db.reference(username + "/password").get()
        change_password_logic(x, username, confirmation)
        i += 1

      elif (i > int(args[1]) - 1):
        break

      else:
        i += 1

  except:
    return print("ERROR: Invalid argument!")