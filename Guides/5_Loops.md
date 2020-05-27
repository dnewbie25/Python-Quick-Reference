# Loops

Loops are intended to create a repetitive block of code that will execute until a certain condition is completed.

As with **if...else** statements, loops need a boolean data type to check if the condition was completed or not in order to finish its execution, otherwise it'll keep running forever.

The basic types of loops are **while** and **for** loops. This is a relatively large section, so you can go directly to [While loops](#while-loops) or [For loops](5_Loops.md#for-loops).

## While Loops

This kind of loops can be executed forever if the condition to evaluate is True. Once the condition is False it will stop.

~~~python
x = 0

while x < 10:
  print(f"Execution #{x}")
  x+=1 # It's very IMPORTANT to increase or decrese the value being evaluated so this loops doesn't run forever
  
# This will print the digits from 0 to 9
~~~

### break Statement

You can use a break statement, no matter if it's inside the loop or nested within an **if...else** statement or a loop inside another loop to tell Python to stop the execution of the loops. (So much 'loop' in a single sentence)

~~~python
while True: # This won't stop, never
  print("Please type your name")
  name = input()
  if name == "Maria":
    break  # This code will keep executing until the user enters 'Maria' as her name
print("Thank you") 
~~~

### continue Statement

When the program reaches a **continue** statement, it jumps back to the start of the loop and reevaluates the loop's condition.

~~~python
while True: # Keeps running forever
  print("Who are you?")
  name = input()
  if name != "Joe":
    continue  # If name is different from 'Joe' it will start the loop again
   else:
     print("Hi! " + name)
     break   # If the name is 'Joe' it will print the message and exit the loop, then prints 'Welcome!!'
 print("Welcome!!") 
 ~~~

### Truthy and Falsy values

Depending on the conditions evaluated an expression could be **True** or **False**, not both. But there are some values than Python determines as **False**. These are:

**0** A zero will be evaluated as False, **number = 0 is False**

**0.0** The same for float zero, **x = 0.0 is False**

**'' or ""** The empty string will be False, **name = '' or name = "" both are False**

A perfect example for Truthy of Falsy values is:

~~~python
name = '' # Is False
while not name: # not name could be written as not(name) which is True
 print('Enter your name:')
 name = input() # If the user enters a blank string (a backspace because even a single space is considered a character) without typing anything else, the loop will start all over again
print('How many guests will you have?') # Once the user enters a name, the loop will stop and the program will continue executing
numOfGuests = int(input())
 if numOfGuests:
  print('Be sure to have enough room for all your guests.')
print('Done')
~~~

### else Statement

Yes, you read correctly, you can use an **else** within a while loop to execute a line of code once the condition is no longer True.

~~~python
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
~~~

## For Loops

A **for** loop will execute a specified number of times, opposite to a **while** loop which can be executed forever as long as the condition is True.

One of the key elements of a **for** loop is the function **range( )**, which determines how many times will the for loop execute.

### range( ) Starting, Stopping, and Stepping Arguments

**Starting and Stopping**

If you want a block of code to be executed 6 times, you should do it like this:

~~~python
for i in range(6): # The i is the counter in the loop, once i is equal to 6 the for loop will stop. The counter starts as 0
  print("Hello #" + str(i)) # This will print, in a new line each time, 'Hello #0', 'Hello #1'....'Hello #5'
~~~

You can change the value of *i* by initializing before the for loop, but you can also specify a range inside the **range( )** function, like this:

~~~python
for i in range(5, 10):
  print("i is now " + str(i))
~~~

**NOTE:** Keep in mind the the range function is inclusive-exclusive. In set operations if would be [x,y). This means it will include the first value and not the last value. It range() has only one parameter, it will start as zero (or whatever value 'i' is equal to) and stop before reaching the exact parameter's value.

**Stepping or Customized jumps**

The **range( )** will add 1 to the 'i' variable everytime, but if you want to add 2, 3 or 4 to that variable you can do it by adding a third parameter to our counter (So if you just needed 1 argument to start at zero, not you need to specify it so it won't get confussed with a range withint the range( ) function).

~~~python
# We  want to count from 0 to 15, adding three every time
for i in range(0, 16, 3): # Remember that for is inclusive-exclusive, and because we want 15 to get printed we need to stop the loop at 16
  print(i)  # Prints in a new line each value 0, 3, 6, 9, 12, 15
~~~

### You can loop through a string or a list

By replacing **range( )** with the name of the string or list you are telling python to loop from 0 all the way through the length of that string or list. You can see this in action in the following **Break and Continue** section.

### Break and Continue

Just like a **while** loop you can stop of jump back to the beginning of the loop by using the **break** or **continue** statements.

**break**

~~~python
fruits = ["apple", "banana", "cherry"]
for i in fruits: # As you can see, fruits is used as the range
  print(i)  # i will take the value of the index, apple, banana or cherry
  if i == "banana": 
    break # It will stop the loop if i equals 'banana'
~~~

**continue**

~~~python
fruits = ["apple", "banana", "cherry"]
for i in fruits:
  if i == "banana":
    continue  # This one will jump back to the start of the loop, so once it reaches 'banana' it will stop there and start with the next item
  print(i)  # This will print 'apple', 'cherry'
~~~

## else Statement

As with **while** loops, **for** loops can have an else statement inside to tell the computer to execute a block of code if the loop has finished.

~~~python
for x in range(6):
  print(x)
else:
  print("Finally finished!") # Will print this line once the looping finishes
~~~

## pass Statement

This one is aimed to loops that don't have anything inside them in order to prevent getting an error because a loop cna't be empty.

~~~python 
for x in [0, 1, 2]:
  pass
~~~
