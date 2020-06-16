'''Exception Handling'''

def sum(num1, num2):
  return num1 + num2

def substract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

choice_1 = int(input("Enter number 1: "))
choice_2 = int(input("Enter number 2: "))

operation = input("Enter the operation you want to perform (sum, substract, multiply, divide): ")

if operation == 'sum':
  sum(choice_1, choice_2)
elif operation == 'substract':
  substract(choice_1, choice_2)
elif operation == 'multiply':
  multiply(choice_1, choice_2)
elif operation == 'divide':
  divide(choice_1, choice_2)
else:
  print("Operation Invalid!")