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
  print("Work in progress")


#Update Event
def update_event():
  print("Work in progress")

#Delete Event
def delete_event():
  print("Work in progress")


#Main
def start_calendar():
  welcome()
  start = True
  while start == True:
    user_choices = {"V":view_calendar, 
                    "A":add_event, 
                    "U":update_event,
                    "D":delete_event,
                    "X":exit}
    user_choice = input("""
    A: Add
    U: Update
    V: View
    D: Delete
    X: Exit
    Input: """)
    user_choice = user_choice.upper()
    if user_choice == "V":
      view_calendar()
    elif user_choice == "A":
      add_event()
    elif user_choice == "U":
      update_event()
    elif user_choice == "D":
      delete_event
    elif user_choice == "X":
      exit()


      


start_calendar()
