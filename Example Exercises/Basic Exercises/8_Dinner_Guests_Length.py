# This is where functions beccome useful. We can just copy the function from exercise 3 to input names

guests = [] # Creates an empty list

def invitees_name(): 
  print("Add someone you want to invite:")
  my_guest = input() # Gets the input
  return my_guest.title() # Capitalize it correctly

guests.append(invitees_name())  # Use the function as many times you want
guests.append(invitees_name())
guests.append(invitees_name())

print(len(guests)) # Prints the number of invitees to your party