# Number served
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
    

my_restaurant = Restaurant('McDonals', 'Fast Food')
you_restaurant = Restaurant("Domino's", 'Pizza')
other_restaurant = Restaurant("Archie's", 'Sandwiches')

print(my_restaurant.number_served) # How may orders have my restaurant served?
my_restaurant.set_number_served(15)
print(my_restaurant.number_served)

# Here we add the order increment
my_restaurant.increment_number_served(25)
print(my_restaurant.number_served)

print("\n\n------------------------Login Attempts----------------------------------\n\n")

class User:
  def __init__(self, first_name, last_name, email, phone, city):
    # Define the attributes
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.phone = phone
    self.city = city
    self.login_attempts = 0 # Create attribute login_attempts

  def greet_user(self):
    print("Hi!!!")
    
  def describe_user(self):
    print(f" - You are {self.first_name} {self.last_name}. You email is {self.email} and you phone number is {self.phone}. You currently live in {self.city}")

  # Add a login method

  def increment_login_attempts(self):
    # Increments the login attempts by 1
    self.login_attempts += 1

  # Create a reset method for the login attempts
  def reset_login_attemtps(self):
    self.login_attempts = 0

user_1 = User('Martha', 'Stewart', 'marthaS189@gmail.com','5554012','Phoenix')

print(user_1.login_attempts)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)
# Here we reset the value to 0
user_1.reset_login_attemtps()
print(user_1.login_attempts)