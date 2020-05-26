# Numbers

**Numbers** will be, along with **Strings** and **Boolean**, the most used data types you'll encounter in you development path. But don't worry, you don't to be a math genius to program, just play around and familiarise yourself with some basic math methods.

Before anything else, remeber there are two basic number type, **Integers** and **Floats** that you can see in the [Variables](Variables.md) section.

## Long numbers with '_'

You can use underscores '_'_ to separate large numbers. Python will think it's a regular number without underscores.

~~~python
number = 14_000_000_000_000_000 # It will be easier for people to read this number
print(number) #Print '14000000000000000' because Python will ignore the underscores
~~~

## CONSTANTS

A constant is a number that won't change during the execution of the program. Python doesn't differentiate constant from regular numbers, so a good practice is to use a variable name with all capital letters for constants so you can recognize them easily.

~~~
MY_CONSTANT = 14521
~~~

## Arithmetic

Arithmetic in Python is as simple as regular arithmetic, with pen and paper.

**Adition**

x = 2 + 5 

**Substraction**

x = 2 - 1

**Multiplication**

x = 3 * 8

**Division** 

Keep in mind that every division will return a float number.

x = 7 / 1 --> This will print 7.0

**Modulus**

x = 10 % 2

**Exponentiation**

x = 4 ** 2

**Floor Division**

Floor division rounds the result DOWN to the nearest whole number.

x = 15 // 2 --> This is equals to 7.5 but the floor division will return 7

## Assignment Operations

An assignment operator, besides '=' which assigns the value to the right into the variable to the left, x = 5, there are a handful of operators used to change the value of a varibale by another value that depends of the same variable. Let's take a look:

**+=** 

If x = 5, then *x += 10* equals to *x = x + 10*, which is 15.

**-=**

If x = 5, then *x -= 10* equals to *x = x - 10*, which is -5. 

So:

***=**  -->   x = x * y   -->   x *= y

**/=**  -->  x = x / y   -->   x /= y

**%=**  -->   x = x % y  -->  x %= y

**//=**   -->   x = x // y   -->   x //= y
