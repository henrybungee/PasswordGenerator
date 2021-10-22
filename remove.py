from firebase_admin import db
import os
import getpass

def remove_password(username, ref, args):
  try:
    passRef = db.reference(username + "/passwords/")
    passWords = passRef.get()
    
    i = 0

    for x in passWords:
      if (i == int(args[1]) - 1):
        confirmation = db.reference(username + "/password").get()
        while True:
          confirmInput = getpass.getpass("Enter password to remove this password:\n")
          if (confirmInput == confirmation):    
            passWordRef = db.reference(username + "/passwords/" + x)

            passWordRef.delete()
            print("Password " +x+ " deleted.")
            break
          else:
            print("Wrong password!")
      i += 1

  except:
    return print("ERROR: Invalid argument!")