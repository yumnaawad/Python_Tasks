import string
import random
while True:
    try:
        lenght = int(input("PLEASE ENTER A PASSWORD LENGHT: "))
        if lenght < 5:
            print("Please ENTER A VALID LENGHT:")
        else:
            break
    except ValueError:
        print("Please ENTER A VALID LENGHT:")

while True:
    try:
      charecter_types = int(input("ENTER THE NUMBER NETX TO THE OPTION YOU WANT :: 1- NUMBERS   2- LETTERS  3- LETTERS+NUMBERS 4-LETTERS+NUMBERS+SYMBOLS "))
      if charecter_types ==1:
        password = ''.join(random.choices( string.digits, k = lenght))
        break
      elif charecter_types ==2:
        password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase , k = lenght))
        break
      elif charecter_types ==3:
        password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = lenght))
        break
      elif charecter_types ==4:
        password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k = lenght))
        break
      else :
        print("Please ENTER A VALID choice:")
    except ValueError:
        print("Please ENTER A VALID choice:")


print("YOUR PASSWORD WAS GENERATED ! : " + str(password))
