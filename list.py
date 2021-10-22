import firebase_admin
import os

def list_passwords(ref, username):
  passwords = ref.get()
  i = 0

  try:
    for x in passwords:
      print(str(i + 1) + " - " + x)
      i += 1
  except:
    print("No passwords saved.")
