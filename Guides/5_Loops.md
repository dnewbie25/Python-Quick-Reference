# Loops

Loops are intended to create a repetitive block of code that will execute until a certain condition is completed.

As with **if...else** statements, loops need a boolean data type to check if the condition was completed or not in order to finish its execution, otherwise it'll keep running forever.

The basic types of loops are **while** and **for** loops. 

## While Loops

This kind of loops can be executed forever if the condition to evaluate is True. Once the condition is False it will stop.

~~~python
x = 0

while x < 10:
  print(f"Execution #{x}")
  x+=1 # It's very IMPORTANT to increase or decrese the value being evaluated so this loops doesn't run forever
  
# This will print the digits from 0 to 9
~~~

## break Statement

You can use a break statement, no matter if it's inside the loop or nested within an **if...else** statement or a loop inside another loop to tell Python to stop the execution of the loops. (So much 'loop' in a single sentence)

~~~python
while True: # This won't stop, never
  print("Please type your name")
  name = input()
  if name == "Maria":
    break  # This code will keep executing until the user enters 'Maria' as her name
print("Thank you") 
~~~

## continue Statement

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