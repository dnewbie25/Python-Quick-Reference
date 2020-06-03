# Boolean Algebra

From now on, if and else statements as well as loops and some other methods will use boolean values to evaluate an instruction. Boolean values can be obtained by comparing two or more expressiones with the following comparison operators.

## Truthy and Falsy values

Depending on the conditions evaluated an expression could be **True** or **False**, not both. But there are some values than Python determines as **False**. These are:

**0** A zero will be evaluated as False, **number = 0 is False**

**0.0** The same for float zero, **x = 0.0 is False**

**'' or ""** The empty string will be False, **name = '' or name = "" both are False**

## Comparison Operators

**==** Equals to -->  x == y

**!=** Not equal	--> x != y	

**>**	Greater than -->	x > y	

**<** Less than	--> x < y	

**>=** Greater than or equal to -->	x >= y	

**<=**	Less than or equal to	--> x <= y

## Logical Operators

_**and**_  Returns True if both statements are True, 5 > 0 **and** 4 > 2 

_**or**_  Returns False if both statements are False, otherwise it will return True, 4 <= 2 **or** 3 == 3.0

_**not**_  Returns the opposite value. For exaple 5 > 0 is True, but **not(5 > 0)** returns False

## if Statements

This blocks of code will execute when the condition evaluated is True. Otherwise it will stop and continues to the next block of code.

~~~python
name = input() # The user can input some data, let's say she entered "Rachel"

if name == "rachel":
  print("You can go in") # The statement is False because 'Dave' != 'dave'
~~~

For this reason it's better to convert all input into lower case, so you can evaluate it more easily.

~~~python
user_input = input() # The user can input some data
name = user_input.lower() # Converts to lower case

if name == "rachel":
  print("You can go in, " + name.title()) # Prints 'You can go in, Rachel"
~~~

## else Statement

This executes only when the **if** clause is False.

~~~python
if name == 'Alice':
 print('Hi, Alice.')
else:
 print('Hello, stranger.')
~~~

## elif Statement

It means **else if**. You can use it when you will have more than one clause to evaluate.

~~~python
name = 'Carol'
age = 3000
if name == 'Alice':
 print('Hi, Alice.')
elif age < 12:
 print('You are not Alice, kiddo.')
elif age > 2000:
 print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
 print('You are not Alice, grannie.')
~~~

As you can see, it's not required to finish with an **else**, you can finish a code block with an **elif** as well.

**The order of the if...else...elif statements matters. Once it reaches a clause where the expression can be evaluated to True it will stop the execution of the block of if..else code**

## Identity Operators

These ones are very special, because they evaluate not if the values are the same but if their class or type is the same.

**is**

Evaluates if the class or type is the same.

~~~python
x = 5
if type(x) is int:
  print(str(x) + " is an Integer") # Prints '5 isan Integer'
~~~

**is not**

Evaluates if the class or type is different.

~~~python
x = 101
if type(x) is not float:
  print(str(x) + " is NOT a Float") # Prints '101 is NOT a Float'
~~~

## Membership Operators

Thise ones would be helpful when you want to know if an elements is inside a list or a dictionary...you'll need them later.

**in**

Returns *True* if a sequence of the specified characters is found.

**not in**

Opposito to **in**, returns *True* is the specified element **is not found**.
