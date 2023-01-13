import hashlib
import re


# Function to validate the password
def signupForUser():
  name = str(input("Enter username:"))
  ID = input("Enter id:")
  PhoneNumber = input("Enter PhoneNumber:")
  nationalId = input("Enter  nationalId:")
  email = input("Enter email address:")
  while True:
    pwd = input("Enter a password: ")
    if len(pwd) < 8:
      print("Make sure your password is at lest 8 letters")
    elif re.search('[0-9]', pwd) is None:
      print("Make sure your password has a number in it")
    elif re.search('[A-Z]', pwd) is None:
      print("Make sure your password has a capital letter in it")
    else:
      print("Your password seems fine")
      break
  conf_pwd = input("Confirm password: ")
  if conf_pwd == pwd:
    enc = conf_pwd.encode()
    hash1 = hashlib.md5(enc).hexdigest()
    with open("credentials.txt", 'w') as f:
      f.write(email + "\n")
      f.write(hash1)
    f.close()
    print("You have registered successfully!")
  else:
    print("Password is not same as above! \n")


def signup():
  name = str(input("Enter username:"))
  ID = input("Enter id:")
  email = input("Enter email address:")
  while True:
    pwd = input("Enter a password: ")
    if len(pwd) < 8:
      print("Make sure your password is at lest 8 letters")
    elif re.search('[0-9]', pwd) is None:
      print("Make sure your password has a number in it")
    elif re.search('[A-Z]', pwd) is None:
      print("Make sure your password has a capital letter in it")
    else:
      print("Your password seems fine")
      break
  conf_pwd = input("Confirm password: ")
  if conf_pwd == pwd:
    enc = conf_pwd.encode()
    hash1 = hashlib.md5(enc).hexdigest()
    with open("credentials.txt", 'w') as f:
      f.write(email + "\n")
      f.write(hash1)
    f.close()
    print("You have registered successfully!")
  else:
    print("Password is not same as above! \n")


def login():
  email = input("Enter email: ")
  pwd = input("Enter password: ")
  auth = pwd.encode()
  auth_hash = hashlib.md5(auth).hexdigest()
  with open("credentials.txt", 'r') as f:
    stored_email, stored_pwd = f.read().split("\n")
  f.close()
  if email == stored_email and auth_hash == stored_pwd:
    print("Logged in Successfully!")
  else:
    print("Login failed! \n")


def Centers_Admin():
  def Search():
    file = open("VaccinationCenter.txt", 'w')
    VaccinationCenter = [
    "Nasr City", "Doki", "October", "Down Town", "Bolak Eldakror", "Helwan",
    "Maadi", "Bohooth", "Baragil"
    ]
    s = input("Enter an place to be search:")
    i = 0
    f = 0
    while (i < len(VaccinationCenter)):
      if s == VaccinationCenter[i]:
        f = 1
        print(VaccinationCenter[i])
      i += 1
    if f == 0:
      print("no")


  def Add():
    VaccinationCenter = [
    "Nasr City", "Doki", "October", "Down Town", "Bolak Eldakror", "Helwan",
    "Maadi", "Bohooth", "Baragil"
    ]
    x = input("Place for add in centers: ")
    i =0
    error=0
    VaccinationCenter.insert (len(VaccinationCenter),x)
  

  def Remove():
    VaccinationCenter = [
    "Nasr City", "Doki", "October", "Down Town", "Bolak Eldakror", "Helwan",
    "Maadi", "Bohooth", "Baragil"
    ]
    x = input("Place for add in centers: ")
    i =0
    error=0
    VaccinationCenter.remove (len(VaccinationCenter),x)
  while 2:
    ch = str(input("Enter your choice: "))
    print("1.Search about center")
    print("2.Add Center")
    print("3.Remove Center")
    print("4.Exit")
    ch = str(input("Enter your choice: "))
    if ch == '1':
      Search()
    elif ch == '2':
      Add()
    elif ch == '3':
      Remove()
    elif ch == '4':
      break
    else:
      print("Wrong Choice!")


def Centers_User():
  VaccinationCenter = [
    "Nasr City", "Doki", "October", "Down Town", "Bolak Eldakror", "Helwan",
    "Maadi", "Bohooth", "Baragil"
  ]
  #print("The centers is",VaccinationCenter)
  print("The centers is :\n ")
  for i in VaccinationCenter:
    print(i, end='\n')


while 1:
  print("****** Vaccination Scheduling System ******")
  print("1.Admin")
  print("2.User")
  print("3.Exit")
  ch = str(input("Enter your choice: "))
  if ch == '1':
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = str(input("Enter your choice: "))
    if ch == '1':
      signup()
      Centers_Admin()
    elif ch == '2':
      login()
      Centers_Admin()
    elif ch == '3':
      break
    else:
      print("Wrong Choice!")
  elif ch == '2':
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = str(input("Enter your choice: "))
    if ch == '1':
      signupForUser()
      Centers_User()
    elif ch == '2':
      login()
      Centers_User()
    elif ch == '3':
      break
    else:
      print("Wrong Choice!")
  elif ch == '3':
    break
  else:
    print("Wrong Choice!")





#VaccinationCenter = ["Hepatitis B1", "Rotavirus2 ", "Diphtheria, tetanus, & acellular pertussis3","Haemophilus influenzae type b4","Pneumococcal conjugate5","Inactivated poliovirus6","Influenza7","Influenza7"]
