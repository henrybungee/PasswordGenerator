from firebase_admin import db
import os
import getpass

def view_password(ref, username, args):

  try:
    passRef = db.reference(username + "/passwords/")
    passWords = passRef.get()
    
    i = 0

    for x in passWords:
      if (i == int(args[1]) - 1):
        confirmation = db.reference(username + "/password").get()
        while True:
          confirmInput = getpass.getpass("Enter password to view password:\n")
          if (confirmInput == confirmation):    
            passWordRef = db.reference(username + "/passwords/" + x + "/saved_password").get()
            #os.system("clear")
            print("Your password is: " +passWordRef)
            break
          else:
            print("Wrong password!")
      i += 1

  except:
    os.system("clear")
    return print("ERROR: Invalid argument!")