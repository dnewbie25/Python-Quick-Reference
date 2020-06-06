# Classes

You have seen that a function is useful when you want to perform a task without having to type all the code more than once. **Object-oriented programming** is the foundation of modern programming, allowing people to represent real-world problems to a computer in order to get the desired output.

When creating a **Class** you are actually creating a "blueprint" which you can then duplicate (**instantiate**) into an **object**. An **object** belongs to a particular **class**. You work with the **instances** of an object.

You can specify information for every instance and a set of actions every instance can perform. You'll save classes inside modules and you can create classes that extend the functionality of another classes to make your code more efficient.

## Creating and Using a Class

The basic example you will definitely find in almost every programming book is the *Dog* class. You can create a class to represent a dog in real life. As any dog, you have to specify its race, name and age as well as its behavior, sit, roll over, bark, greets.

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

**1 - ** The class *Dog* is created. As convention every class name should be capitalized.

**2 - ** A function that's part of a class is called a *method*...actually function and name are the same, but it's better to point that because some programmers are very strict regarding the names they use, so keep this in mind.

The *__init__()* is a special method that Python runs automatically every time we create an instance (copy) of the Dog class. You need to use **two underscores at the beginning and at the end of the method to make Python run it automatically**.

**Parameters inside __init__()**: This method has a special parameter, **self**. This one gives access to the instance to every function in the class it is calling. When we cant to use the Dog class we will pass only name and age because *self* will run automatically.

**3 - ** We create a method sit() with the parameter *self*. This way the sit method will have access to a variable that was defined in the function *__init__*. Remember there are local and global variables. The *self* allows every function inside the class to access the variables inside the *__init__()*.

Variables that are accesible through instances like this are called **attributes**.

