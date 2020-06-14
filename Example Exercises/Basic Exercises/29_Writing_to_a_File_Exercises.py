from datetime import date, timedelta # In order to use the current day and add days to it
from random import randint # To add a random number to current date

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

'''while loop_2 < 5:
  name =  ask_name()
  with open(filename_2, 'a') as guests_book:
    guests_book.write(f"{name.title()} has visited the hotel on {str(today + timedelta(days=day))}\n\n")

  loop_2 += 1
  day += (randint(0, 30))''' # Works great

# Programming Poll

filename_3 = 'Files Samples/programming_poll.txt'

choice = ''
yeses = 0
noes = 0
invalid = 0

while choice != 'quit':
  my_vote = input("You love programming? Yes or No\nIf you want to quit just type 'quit': ")
  my_opinion = ''

  if my_vote.lower() == 'quit':
    break
  elif my_vote.lower() == 'yes':
    yeses += 1
    my_opinion = input("Enter you opinion about programming: ")
  elif my_vote.lower() == 'no':
    noes += 1 
    my_opinion = input("Enter you opinion about programming: ")
  else:
    invalid += 1


  with open(filename_3, 'a') as poll:
    poll.write(f"{my_opinion.title()}\n")

with open(filename_3, 'a') as total_votes:
  total_votes.write(f"The total of votes were YES - {yeses}, NO - {noes} and INVALID - {invalid}")