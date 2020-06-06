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


my_dog = Dog('Maxy', 5) # Creates an instance of the class Dog

print(f"My dog's name is {my_dog.name}") # Calls an attribute, in this case name
print(f"It's {my_dog.age}") # Calls an attribute, in this case age

my_dog.sit() # Calls the sit() method
my_dog.roll_over() # Calls the roll_over() method