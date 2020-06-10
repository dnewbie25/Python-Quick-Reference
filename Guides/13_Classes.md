# Classes

You have seen that a function is useful when you want to perform a task without having to type all the code more than once. **Object-oriented programming** is the foundation of modern programming, allowing people to represent real-world problems to a computer in order to get the desired output.

When creating a **Class** you are actually creating a "blueprint" which you can then duplicate (**instantiate**) into an **object**. An **object** belongs to a particular **class**. You work with the **instances** of an object.

You can specify information for every instance and a set of actions every instance can perform. You'll save classes inside modules and you can create classes that extend the functionality of another classes to make your code more efficient.

## Creating and Using a Class

The basic example you will definitely find in almost every programming book is the *Dog* class. You can create a class to represent a dog in real life. As any dog, you have to specify its breed, name and age as well as its behavior, sit, roll over, bark, greets.

In this example we will create a dog with two pieces of information and two behaviors:

~~~python
class Dog: # 1

  def __init__(self, name, age): # 2
    # Initialize name and age
    self.name = name
    self.age = age
  
  def sit(self): # 3
    # Simulate the dog sitting in response to a command
    print(f"{self.name} is now sitting.")
    
  def roll_over(self): # 4
    # Simulates the dog rolling over after a command is given to it
    print(f"{self.name} rolled over!")
~~~

You see that there are some numbers after each statement. I'll explain what's happening there:

**1-** The class *Dog* is created. As convention every class name should be capitalized.

**2-** A function that's part of a class is called a *method*...actually function and name are the same, but it's better to point that because some programmers are very strict regarding the names they use, so keep this in mind.

The *__init__()* is a special method that Python runs automatically every time we create an instance (copy) of the Dog class. You need to use **two underscores at the beginning and at the end of the method to make Python run it automatically**.

**Parameters inside __init__()**: This method has a special parameter, **self**. This one gives access to the instance to every function in the class it is calling. When we cant to use the Dog class we will pass only name and age because *self* will run automatically.

**3 and 4-** We create a method sit() with the parameter *self*. This way the sit method will have access to a variable that was defined in the function *__init__*. Remember there are local and global variables. The *self* allows every function inside the class to access the variables inside the *__init__()*.

Variables that are accesible through instances like this are called **attributes**.

## Making an Instance from a Class

The best explanation I have ever read about this is, "think of a class a set of instructions for how to make an instance".

For example, the class *Dog* is just a set of instructions about how to make individual instances(copy) representing specific dogs.

~~~python
class Dog:
  # Here you defined the information and behavior of the dog
  
my_dog = Dog('Willie', 6) # You create one instance of the Dog class, called my_dog 

print(f"My dog's name is {my_dog.name}.") # This will use the values defined for my_dog as arguments for the parameters of the methods defined inside the class Dog
print(f"My dog is {my_dog.age} years old.") # Same here
my_dog.sit() # Calls the sit() method for the new instance of Dog
my_dog.roll_over() # Calls the roll_over() method for the new instance of Dog

# It prints:
'''
My dog's name is Maxy
It's 5
Maxy is now sitting
Maxy is rolling over!!
'''
~~~

### Accessing the Attributes

As you saw in the previous example, when you want to access to the attributes (information) in a class you use the dot notation, like **my_dog.name**. This then refers to the attribute named **self.name = name** in the *__init__()* function.

### Calling Methods

Like we said before, you use the dot notation but now you refer to the method you want to call, for example **my_dog.sit()** will call the method *sit()* and will pass the arguments given to *my_dog* in order to execute the method. The same for *roll_over()*.

## Creating Multiple Instances

With the same *Dog* class, let's create multiple instance for dogs (objects or copies with their own attributes but same methods).

~~~python
# Imagine the class was defined here. This in order to simplyfy the amount of text I have to type

my_dog = Dog('Titan', 5)
your_dog = Dog('Puffy', 2)

print(f"My dog's name is {my_dog.name}") # Prints 'My dog's name is Titan"
print(f"Your dog's name is {your_dog.name}") # Prints 'Your dog's name is Puffy"
~~~

You can do the above with methods and any other attribute your class has. Even if you use the same name and age for both dogs Python will read them as two separate instances. It's like two people with the same breed of dog and the same name for them, but you know they are not the same dog.

The only thing you need to differ from each instance is the instance's name, *my_dog* or *your_dog* but you can't name them the same, otherwise you will be redefining it and having just one only instance.

## Working With Classes And Instances

One of the thins you want is to modify the attributes in eery instance you create, because even when you are working with the blueprints of a car like a Mazda 3, you still want to change the color, the number of seats, the speed and the size of the trunk.

This part would take a lot to write, so I decided to create a code example with comments so you can see what's happening. Just go to [Classes And Instances](https://github.com/dnewbie25/Python-Quick-Reference/blob/master/Example%20Exercises/Basic%20Exercises/22_Classes%20_And_Instances.py).

In the previous link you will see how to set a default value for an attribute, how to modify the attribute by using methods, a reset method or just be redefining the attribute in each instance.

## Inheritance

When you are about to write classes that you realize have a pattern in their design or at least they share a particular set of methods or attributes, **inheritance** will be that magic tool that will save you a lot of time and headaches for repeating yourself in many class declarations.

**Inheritance** is giving attributes or methods of a parent class or superclass to a child class or subclass, so for example if we build a class for cars, after a while we realize that even when cars speed up, brake and turn, there are cars with 6 wheels (trucks), two wheels (bikes), amphibious cars, electric cars, etcetera. Yes you speed up, brake and turn left or right with each one but they have in common just that, all their parts were built for that specific type of car.

#### __init___( )

When we create the car class, we know that every car has a make, model and year. These are the common attributes among all types of cars. So we can create a parent class with this attributes and replicate it in all of our types of cars:

~~~python
class Car:
  '''A simple class to model cars'''
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0 # This could vary from used to new cars, so we declare it in __init__ but we don't use it as a mandatory parameter
    
 def get_descriptive_name(self): # Prints car's initial attributes
 long_name = f"{self.year} {self.manufacturer} {self.model}"
 return long_name.title()

 def read_odometer(self): # Reads the odometer
 print(f"This car has {self.odometer_reading} miles on it.")

 def update_odometer(self, mileage): # Change the value of the odometer
 if mileage >= self.odometer_reading:
  self.odometer_reading = mileage
 else:
  print("You can't roll back an odometer!")

 def increment_odometer(self, miles): # Increases the odometer by miles
 self.odometer_reading += miles
~~~

That is our initial class. All vehicles share those attributes. Think about one non-human powered vehicle that doesn't have those characteristics. Bicycles don't count, they are human-powered.

Now, let's create some electric vehicles:

~~~python
class Electric_Car(Car): # Here we say to Electric_Car to inherit the methods and attributes of Car class, so we don't have to write all the previous code again.
  def __init__(self, make, model, year): # Every car has its own make model and year
    super().__init__(make, model, year) # But with this line our method can those 3 attributes with the methods of Car class
    
my_Ecar = Electric_Car('Tesla', 'model s', 2019)
print(my_Ecar.get_descriptive_name()) # You see this is a method of Car class we didn't declare inside Electric_Car. Inheritante allows us to use the parent class methods with our child class attributes
# Prints '2019 Tesla Model S'
~~~

#### Defining Attributes and Methods for the Child Class

After you create a parent and a child class, you can include some attributes unique to child class only. This way we start to create a vehicle that has its own features that no other vehicle has.

Let's custom our electric car a bit:

~~~python
class Electric_Car(Car):
  def __init__(self, make, model, year):
    super().__init__(make, model, year) # We initialize the attributes from the parent class
    self.battery_size = 75 # But electric cars all begin with a battery, in this case a 75 kWh battery
 
  def describe_battery(self):
    print(f"This car has a {self.battery_size} kWh battery")
    
my_Ecar = Electric_Car('Tesla', 'model s', 2019)
print(my_Ecar.get_descriptive_name())
my_Ecar.describe_battery() # Prints 'This car has a 75 kWh battery'
~~~

You can add as many methods and attributes as you want, but if you find that an attribute or method can be used is any other type of car you should add it to the Car parent class.

#### Overriding Methods from the Parent Class

In Python if you have a method in the parent class but don't want to use it exactly like it was declared, you can override it by redeclaring it inside the instance you are creating and changing its attributes or functions inside. Python will disregard the method from the Car class and will use the method declared inside the child class. For example, if we want to change *get_descriptive_name( )* just for Electric_Car we redeclare it:

~~~python
class Electric_Car(Car):
  def __init__(self, make, model, year):
    super().__init__(make, model, year) # We initialize the attributes from the parent class
    self.battery_size = 75 # But electric cars all begin with a battery, in this case a 75 kWh battery
 
  def describe_battery(self):
    print(f"This car has a {self.battery_size} kWh battery")
    
  def get_descriptive_name(self): # We don't want to print '2019 Tesla Model S', we want to change it
    print(f"The new environment friendly {self.make} {self.model} will be available in {self.year}")
    
my_Ecar = Electric_Car('Tesla', 'model s2', 2022)
print(my_Ecar.get_descriptive_name()) # Now it prints 'The new environment friendly Tesla Model S2 will be available in 2022'
my_Ecar.describe_battery() # Prints 'This car has a 75 kWh battery'
~~~

#### Instances As Attributes

As you start modeling real-world objects you will realize than sometimes a class can be separated into smallers classes. For example, an electric car might be created by joining a Battery class, a Brake class, a Self_Drive class because even electric cars vary in battery size, power, speed, acceleration, materials. 

For example, let's create a class for the Battery which we'll use to create a class Electric_Car:

~~~python
class Car: 
  # Assume we created the previous Car class again here

class Battery:
  '''A simple battery for E-cars'''
  def __init__(self, battery_size = 75): # Initialize the battery attributes, by default batteries come in 75 kWh models
    self.battery_size = battery_size
    
  def describe_battery(self):
    """Print a statement describing the battery size."""
    print(f"This car has a {self.battery_size}-kWh battery.")
    
class Electric_Car(Car): # We create the electric car class that inherits from Car
   """Represent aspects of a car, specific to electric vehicles."""
   def __init__(self, make, model, year):
    """
    Initialize attributes of the parent class.
    Then initialize attributes specific to an electric car.
    """
      super().__init__(make, model, year)
      self.battery = Battery() # We use the Battery class as an attribute for this particular electric car
      
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() # My instance calls the battery attribute which then calls the method describe_battery() from the Battery class
~~~
