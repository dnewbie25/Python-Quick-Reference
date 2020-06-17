# Exceptions

Often when you are running  aprogram if you enter an unexpected input, like a letter instead of a number the program will crash. As a user you don't want to read the traceback message to see what happened. Users don't care about troubleshooting because they shouldn't be troubleshooting your pgroam in the first place. Like a car, you don't want to fix a car every time you want to use it.

## Try and Except Statements

Python has two statements in order to work with exceptions. With these ones the user can input incorrect data and the program won't crash. It will continue but a message indicating that the input was incorrect should appear so the user knows exactly what they need to enter in the program.

## Common Exceptions

When you input incorrect data Python will show you an error message in the traceback (the console). These messages indicate the error with a specific name:

### Division by Zero or ZeroDivisionError

This is the perfect example because I think we all have tried this one.

~~~python
print(5/0)
Traceback (most recent call last): # This is a Traceback
 File "division_calculator.py", line 1, in <module>
 print(5/0)
ZeroDivisionError: division by zero # This is the error name
~~~

To handle divisions by zero you can specify that this operation is not allowed:

~~~python
number = int(input()) # Let's say we input 5

try:
  print(number/0) # If no error is generated the program executes this line, which won't be the case with this one
except ZeroDivisionError: # When Python recognizes an error the except block will execute. Like an if-else but the trigger is the error's name you specified
  print("You can't divide by Zero. Correct the operation")
~~~

#### Using Exceptions To Prevent Crashes

You need to handle errors when the program has a lot to do. You need to be aware of possible errors when your program starts, when it is running or finishing.

A short example:

~~~python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True: 
 first_number = input("\nFirst number: ") # Enter first number
 if first_number == 'q':
  break # Exit if enter 'q'
 second_number = input("Second number: ") # Enter second number
  if second_number == 'q':
    break
answer = int(first_number) / int(second_number) # Divide the first one by the second one
print(answer)
~~~

#### else Statement

As the previous example, if the user enters 7 and 0 the program will crash. A way to use **try-except** within a program is this:

~~~python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True: 
 first_number = input("\nFirst number: ") # Enter first number
 if first_number == 'q':
  break # Exit if enter 'q'
 second_number = input("Second number: ") # Enter second number
  if second_number == 'q':
    break # Exit if enter 'q'
  try:
      answer = int(first_number) / int(second_number) # Divide the first one by the second one
  except ZeroDivisionError: # If the second one is zero it prints this message
      print("You enter a zero as the second number. Can't divide by Zero!")
  else:
    print(answer) # If the try was successful it continues to this block and prints the answer
~~~

Note that we have an **else** statement too, but here it works different from **if-else**. When you use an **else** in exception handling you are telling Python that once the code in the *try* block executes, if no error occurs, then continue with the code inside the *else* statement. It isn't so required with modern Python versions but it can be helpful.

### FileNotFound Exception

You can tell by its name what it refers to. When you try to read a file or perform any change to it, if the file is not in the specified directory you will encaounter this message.

~~~python

filename = 'Pictures/alice.txt'

with open(filename) as book:
  read_book = book.read()
  
'''This will print
Traceback (most recent call last):
 File "alice.txt", line 3, in <module>
 with open(filename) as book:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt' 
'''
~~~

Our file turns out to be in the Download folder, not in the Pictures folder. So you can put an exception like this:

~~~python
filename = 'Pictures/alice.txt'
try: # If no error arises the program will execute
  with open(filename) as book:
    read_book = book.read()
except FileNotFound: # Otherwise it will print this message
  print(f"The file is not in the directoy. Please check and change the folder")  
~~~

## Analyzing Text

