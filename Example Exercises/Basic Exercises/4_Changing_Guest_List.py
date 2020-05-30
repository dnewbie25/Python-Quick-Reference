print("Add the people you want to invite. Remember they must have first name and last name.")

guests = [] # Creates an empty list

def invitees_name(): # We don't want to type the same code three times. So we create a function
  print("Add someone you want to invite:")
  my_guest = input() # Gets the input
  return my_guest.title() # Capitalize it correctly

guests.append(invitees_name())  # Use the function as many times you want
guests.append(invitees_name())
guests.append(invitees_name())

print(guests)
for i in guests: # Prints the value of each index 
  print(f"I would like to invite you, {i} to my party this Saturday!")

########## Here the exercise begins ##############

import random # We will let the computer to choose a random person not allowed to go to the party

computer_evil_choice = random.randint(0,3) # Remember we have just 3 invitees and this range in inclusive-exclusive

for guests_in_list in guests: # This will loop through every person in the list

  # If the person is the same the computer chose, we replace her with the new input
  if guests_in_list == guests[computer_evil_choice]:
    print(f"Looks like you have to invite someone else instead of {guests[computer_evil_choice]}\n"+
      "Please enter a new guest:")
    new_guest = input()
    new_guest = new_guest.title()
    guests[computer_evil_choice] =  new_guest
    break
  


print("Now the new invitations are:")

for i in guests: # Prints the value of each index 
  print(f"I would like to invite you, {i} to my party this Saturday!")