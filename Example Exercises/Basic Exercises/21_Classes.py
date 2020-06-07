class Dog:
  """Create a class Dog"""
  def __init__(self, name, age):
    '''Initialize name and age attributes'''
    self.name = name
    self.age = age

  def sit(self):
    # Simulates sitting
    print(f"{self.name} is now sitting")

  def roll_over(self):
    # Simulates rolling over
    print(f"{self.name} is rolling over!!")

'''
my_dog = Dog('Maxy', 5) # Creates an instance of the class Dog

print(f"My dog's name is {my_dog.name}") # Calls an attribute, in this case name
print(f"It's {my_dog.age}") # Calls an attribute, in this case age

my_dog.sit() # Calls the sit() method
my_dog.roll_over() # Calls the roll_over() method
'''

print("-------------------------------------------------\n\n")
'''Try it yourself. Class Restaurant'''

class Restaurant:
  '''Create a class for Restaurant'''
  def __init__(self, restaurant_name, cuisine_type): 
    # Define the attributes
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print(f"My restaurant is {self.restaurant_name}")
    print(f"We are focused on {self.cuisine_type} food")

  def open_restaurant(self):
    print("We are open now!")

# Instance of class Restaurant

restaurant = Restaurant('Chinese Diamond', 'Chinese')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())

# 3 more instances

my_restaurant = Restaurant('McDonals', 'Fast Food')
you_restaurant = Restaurant("Domino's", 'Pizza')
other_restaurant = Restaurant("Archie's", 'Sandwiches')

print(my_restaurant.describe_restaurant())
print(you_restaurant.describe_restaurant())
print(other_restaurant.describe_restaurant())
print("-------------------------------------------------\n\n")

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

# Create an instance 

user_1 = User('Martha', 'Stewart', 'marthaS189@gmail.com','5554012','Phoenix')

print(user_1.greet_user())
print(user_1.describe_user())
  





    