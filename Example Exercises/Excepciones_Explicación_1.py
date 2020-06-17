'''Exception Handling'''

def sum(num1, num2):
  return num1 + num2

def substract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

'''def divide(num1, num2):''' # Si el denominador es cero esto va a causar un crash
'''return num1 / num2'''

# Para evitar eso usamos un try - except

def divide(num1, num2):
  try:
    return num1 / num2
  except ZeroDivisionError:
    print("No se puede dividir entre cero")
    return "Operación incorrecta"

# También si el usuario ingresa letras en lugar de número va a dar un ValueError. Esto se puede corregir así:

while True:
  try:

    choice_1 = int(input("Enter number 1: "))
    choice_2 = int(input("Enter number 2: "))
    break  # Si se ingresan los valores correctos, o sea números, el programa va a salir del loop
  except ValueError:
    print("Los valores ingresados son incorrectos. Intenta con números enteros.") # Si no, se ejecutará el except y volverá a ejecutar el while loop

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