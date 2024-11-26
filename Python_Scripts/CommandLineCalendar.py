from time import sleep,strftime,gmtime

calendar = {}

#Welcome the User
def welcome():
  users_name = input("What is your name: ")
  print("Welcome to the Commandline Calendar " + users_name + "! The program is just starting up...")
  sleep(1)
  print(strftime("%A: %B %d %Y")) #format: Full weekday name Month Day, Year.
  print(strftime("%H:%M:%S", gmtime())) #H:M:S central time
  print("What would you like to do?")


#View Calendar
def view_calendar():
  if len(calendar.keys()) < 1:
    print("Man, you have no friends huh? ")
  else:
    print("Wow, you've got a lot on your plate! ")
    print(calendar)


#Add Event
def add_event():
  None


#Update Event
def update_event():
  None

#Delete Event
def delete_event():
  None


#Main
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
    user_choices = {"V":view_calendar(), 
                    "A":add_event(), 
                    "U":update_event(),
                    "D":delete_event(),
                    "X":exit()}
    
