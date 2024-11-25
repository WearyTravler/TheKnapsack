from time import sleep,strftime,gmtime

calendar = {}


def welcome():
  users_name = input("What is your name: ")
  print("Welcome to the Commandline Calendar " + users_name + "! The program is just starting up...")
  sleep(1)
  print(strftime("%A: %B %d %Y")) #format: Full weekday name Month Day, Year.
  print(strftime("%H:%M:%S", gmtime())) #H:M:S central time
  print("What would you like to do?")


def start_calendar():
  welcome()
  start = True
  while start == True:
    user_choice = input("""
    A: Add
    U: Update
    V: View
    D: Delete
    X: Exit""")
    user_choice = user_choice.upper()
    
