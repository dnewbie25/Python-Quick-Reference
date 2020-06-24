# Testing Code

Python offers a module in order to test our code so we can make sure every line does exactly what we want it to do.

## unittest Module

The module **unittest** offers programmers a powerful tool to make debugging to their code in order to solve any issue even before executing the whole program.

This relies on two methods called **Unit Testing** and **Test Cases**.

**Unit Test**: Ensures that one specific aspect of a function is correct.

**Test Case**: It's a collection of unit tests to make sure that the whole function is correct.

A good test case is when you use every all possible inputs a user might enter to your program to see what happens to that function.

#### unittest Syntax

This is a little cumbersome but once you get used to it by using it a couple times you'll save tons of hours debugging code.

Let's create two programs, one will serve as a module and the other one as the program using that module.

**Module name_function.py**

~~~python
def get_formatted_name(first, last):
  """Generate a full name"""
  fullname = f"{first} {last}"
  return fullname.title()
~~~

**Program using that module, names.py**

~~~python
from name_function import get_formatted_name # We just have one function in that module so it's optional to use this syntax

print("Enter 'q' at any time to exit.")
while True:
  first = input("Enter your first name: ")
  if first == 'q':
    break
    
  last = input("Enter your last name: ")
  if last == 'q':
    break
    
  formatted_name = get_formatted_name(first, last)
  print("\tThe formatted name is: {formatted_name}") # If you enter 'daVid flYncH', it will print 'David Flynch'
~~~

**Now the tricky part, the unittest block of code***

We want to test the previous *name_function.py* module so:

~~~python
import unittest # We import the unittest module
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase): # We create a class NameTestCase that inherits from one of the classes from the unittest module, TestCase
  """Test name_function.py"""
  
  def test_name_function(self): # Define a method to test the names
    formatted_name = get_formatted_name('davId', 'flYncH') # We call the function here
    self.assertEqual(formatted_name, 'David Flynch') # assertEqal compares the function we call with an expected output, in this case we want it to print 'David Flynch'
    
if __name__ == '__main__': # This is somewhat hard to understand at first, but the easy definition: If you use this the unittest will execute just the functions you want to get executed. In larger programs this is helpful because when importing modules you might have some functions executing without you calling them
  unittest.main()
~~~

All of the above will output:

~~~python
.

-----------------------------------------------------

Ran 1 test in 0.000s
OK 
~~~

That means that the program returned the expected output (the one at *self.assertEqual*) and it's OK.

#### Failing Test

Now, when you use the *unittest* module it'll become really common to get errors, because you create it to find errors that you'll certainly have. Let's see how an error is displayed.
