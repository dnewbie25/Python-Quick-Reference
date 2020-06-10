# We use the Restaurant class from 23_Class_Instance_Exercises.py

class Restaurant:
  '''Create a class for Restaurant'''
  def __init__(self, restaurant_name, cuisine_type): 
        # Define the attributes
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0

  def describe_restaurant(self):
    print(f"My restaurant is {self.restaurant_name}")
    print(f"We are focused on {self.cuisine_type} food")

  def open_restaurant(self):
    print("We are open now!")

  def set_number_served(self, orders):
    # Set the number of orders the restaurant has served
    self.number_served = orders

  def increment_number_served(self, increment):
    # Increment the orders
    self.number_served += increment

class IceCreamStand(Restaurant): 
  '''Create a class for an ice cream stand that inherits from Restaurant'''
  def __init__(self, stand_name, type_iceCream):
    super().__init__(stand_name, type_iceCream) # We initialize with the parameters of Restaurant, a name and a kind of cuisine, in this case name of the stand and type of ice cream

  def flavors(self, stand_flavors = []):
    for i in range(5):
      print("Enter a flavor: ")
      flavor = input()
      stand_flavors.append(flavor)

    print("\nMy Ice Cream stand has these flavors:")
    for items in stand_flavors:
      print(f" - {items}")

my_stand = IceCreamStand('Frito Helado', 'Gellato')
print(my_stand.describe_restaurant())
my_stand.flavors()

print("\n\n---------------------------Admin Exercise-------------------\n\n")

# class User

class User:
  def __init__(self, first_name, last_name, email, phone, city):
    # Define the attributes
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.phone = phone
    self.city = city

  def greet_user(self):
    print("Hi!!!")
    
  def describe_user(self):
    print(f" - You are {self.first_name} {self.last_name}. You email is {self.email} and you phone number is {self.phone}. You currently live in {self.city}")

class Admin(User): #Inherits from User
  def __init__(self, first_name, last_name, email, phone, city):
    super().__init__(first_name, last_name, email, phone, city) # Will use the attributes of the User class
    #self.privileges = ["can add post", "can delete post", "can ban users"] # There are 3 types of privileges. This is now in class Privilege
    self.privileges = Privilege()
  

'''my_user = Admin('Danielle', 'Singh', 'dsignh78@hotmail.com', '3254112', 'Dubai')
my_user.describe_user()
my_user.privileges.show_privileges()
''' # This won't work because Privilege was defined after creating my_user. You can't call methods of classes declared after creating the instance


print("\n\n---------------------------Privilege Exercise-------------------\n\n")

class Privilege: # This class will be used as an attribute for Admin class
  def __init__(self, privileges = ["can add post", "can delete post", "can ban users"]): # Initialize the attribute for Privilege
    self.privileges = privileges

  def show_privileges(self):
    my_user_is = input("Choose standard or admin: ")
    if my_user_is.lower() == 'standard':
      print(f"My user {self.privileges[0]} and {self.privileges[1]}")
    elif my_user_is.lower() == 'admin':
      print(f"My user {self.privileges[0]}, {self.privileges[1]} and {self.privileges[2]}")
    else:
      print(f"The type of user '{my_user_is.lower()}' does not exist")

my_user_2 = Admin('Matthew', 'Carlk', 'math34@hotmail.com', '325441', 'Bogota')
my_user_2.describe_user()
my_user_2.privileges.show_privileges()