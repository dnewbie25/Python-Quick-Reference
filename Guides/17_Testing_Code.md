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

**Now the tricky part, the unittest block of code**

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

## Failing Test

Now, when you use the *unittest* module it'll become really common to get errors, because you create it to find errors that you'll certainly have. Let's see how an error is displayed.

Let's say we want to add the second version that adds a middle name only if the person has one.

We can modify the *name_function.py*:

~~~python
def get_formatted_name(first, middle, last):
  fullname = f"{first} {middle} {last}"
  return fullname.title()
~~~

If we apply the test case for this code it will print:

~~~python
E # Means Error
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase) # Tells us what test case failed so we can review that specific code
----------------------------------------------------------------------
Traceback (most recent call last):
 File "test_name_function.py", line 8, in test_first_last_name
 formatted_name = get_formatted_name('janis', 'joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last' # We entered two arguments, it was expecting 3
----------------------------------------------------------------------
Ran 1 test in 0.000s
FAILED (errors=1) # How many test cases failed
~~~

## Responding To A Failed Test

If you have the test case syntax correctly, you will see an error only if the functions it's evaluating failed. **DO NOT TRY TO CHANGE THE TEST CASE TO MAKE IT SAY THE FUNCTION IS OK**. If a test case failed it means you need to change the function it is evaluating, not to change the test case.

In the previous code, there were 3 mandatory parameters, but remember that not everone has a middle name so this parameter should be optional.To do this just move **middle** to the end of the parameters and make it equal to an empty string.

~~~python
def get_formatted_name(first, last, middle = ''):
  if middle: # If middle has something. middle == True won't work because it will evaluate strictly
    fullname = f"{first} {middle} {last}"
  else: # If it's False. An empty string is a Falsy value
    fullname = f"{first} {last}"
    
  return fullname.title()
~~~

Now the test case will print **OK**.

## Adding New Tests

Now, we have a test case for first and last name, but we also want a test case for people with middle names. Let's create another one:

~~~python
import unittest
from name_function import get_formatted name

# The first part is the same we already had
class NameTestCase(unittest.TestCase):
  def test_first_last_name(self):
    fullname = get_formmated_name()
    self.assertEqual(fullname, 'David Flynch')
    
  def test_first_middle_last(self):
    formatted_name = get_formatted_name('David', 'Flynch', 'Theodore')
    self.assertEqual(formatted_name, 'David Theodore Flynch')
    
 if __name__ == '__main__':
  unittest.main()
~~~

The above will print:

~~~python
..
----------------------------
Ran 2 tests in 0.001s
OK
~~~

The test for first and last name as well as the test for first, middle, last name ran without problems. 

# Testing A Class

Previously we tested functions. Now we must go on and start testing classes. You saw the **assertEqual( )** method which evaluates whether an argument is equal to the expected output. There are a lot for assert methods but the main ones are:

**assertEqual(a, b)** evaluates if a == b

**assertNotEqual(a, b)** evaluates if a != b

**assertTrue(x)** evaluates if x is True

**assertFalse(x)** evaluates if x is False

**assertIn(item, list)** evaluates if item is in list

**assertNotIn(item, list)** evaluates if item it not in list

## A Class to Test

Much of this involves just testing the methods inside the class but there are some minor differences that we need to cover. Let's create a simple class:

~~~python
class AnonymousSurvey:

  """Collects anonymous answers to survey questions"""
  
  def __init__(self, question, responses):
    """Store a question and prepares to store answers"""
    self.question = question
    self.responses = []
    
  def show_questions(self):
    """show the survey questions"""
    print(self.question)
    
  def store_response(self, new_response):
    """store a single response to a survey"""
    self.responses.append(new_response)
    
  def show_results(self):
     """Show all the responses given"""
     print("Survey results")
     for response in self.responses:
        print(f"- response")  
~~~
