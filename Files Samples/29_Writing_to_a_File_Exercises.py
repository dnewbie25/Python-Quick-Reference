from datetime import date, timedelta
from random import randint

today = date.today()

# Guests

filename = 'Files Samples/guest.txt'

def ask_name(): # Create a function that asks for the name of the guest
  name = input("What is your guest's name?: ")
  return name

# Creates a while loop for 3 people

loop = 0


'''
with open(filename, 'w') as file_object:
  while loop < 3:
    file_object.write(ask_name().title() + "\n") # Prints name capitalize and adds a new line
    loop += 1''' # Works great


# Guests Book

filename_2 = 'Files Samples/guests_book.txt'

loop_2 = 0
day = 0

while loop_2 < 5:
  name =  ask_name()
  with open(filename_2, 'a') as guests_book:
    guests_book.write(f"{name.title()} has visited the hotel on {str(today + timedelta(days=day))}\n\n")

  loop_2 += 1
  day += (randint(0, 30))