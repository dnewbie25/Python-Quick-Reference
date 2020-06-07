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