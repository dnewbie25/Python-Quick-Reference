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

import random # We will let the computer to choose a random person not allowed to go to the party

computer_evil_choice = random.randint(0,2) # Remember we have just 3 invitees and the range is 0,1,2

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


print("\n\nI just found a bigger Table\n\nWe can invite three mote people!")

# This is were you might confuse. You'll maybe try to insert in positions 0, 1 and 2, but keep in 
# mind that we are adding more people, so the lists is growing.

# We'll end up with 6 people, so the indexes would be 0,1,2...5

guests.insert(0, invitees_name())  # Adds someone at the start of the list
guests.insert(2, invitees_name())   # Adds someone in the middle, it could be index 2 or 3
guests.insert(5, invitees_name())  # Adss someone at the end of the list

for i in guests: # Prints the value of each index 
  print(f"I would like to invite you, {i} to my party this Saturday!")


########## Here the exercise begins ##############


print("\n\nThe table won't arrive on time, so you can invite just two people\n\nDecide:")

removed1 = guests.pop()
print(f"Sorry, {removed1}. You can't come to the party")
removed2 = guests.pop()
print(f"Sorry, {removed2}. You can't come to the party")
removed3 = guests.pop()
print(f"Sorry, {removed3}. You can't come to the party")
removed4 = guests.pop()
print(f"Sorry, {removed4}. You can't come to the party")

print(f"\n\n{guests[0]} and {guests[1]}, you are still invited")

del guests[0]
del guests[1]

print(guests)
