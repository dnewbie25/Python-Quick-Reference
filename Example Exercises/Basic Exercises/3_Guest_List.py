print("Add the people you want to invite. Remember they must have first name and last name.")

guests = [] # Creates an empty list

def invitees_name(): # We don't want to type the same code three times. So we create a function
  print("Add someone you want to invite:")
  my_guest = input() # Gets the input
  return my_guest.title() # Capitalize it correctly

guests.append(invitees_name())  # Use the function as many times you want
guests.append(invitees_name())
guests.append(invitees_name())

for i in guests: # Prints the value of each index 
  print(f"I would like to invite you, {i} to my party this Saturday!")


