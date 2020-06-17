'''Lanzar Excepciones con Raise'''

import math


def evaluar_Edad(edad):

  if edad < 0: # Si la edad es menor a cero, se va a crear una excepción para lo cual usamos raise
    raise ValueError("No se permiten edades negativas")
      
  if edad < 20:
    return "Eres muy joven"
  elif edad < 40:
    return "Eres algo joven"
  elif edad < 65:
    return "Eres maduro" 
  elif edad < 100:
    return "Estás algo mayor, cuídate del covid"
  

#print(evaluar_Edad(85)) # Esto es incorrecto, nadie tiene edad negativa

'''Ahora si no queremos que en programas así las funciones impidan que las siguientes funciones se ejecuten por un error podemos simplemente usar el try-except al momento de llamarlas:
'''

try:
  print(evaluar_Edad(-85))
except ValueError as ErrorNumeroNegativo: # Aquí debe usarse el mismo valor que el raise tiene y se puede usar un alias
  print(ErrorNumeroNegativo) # Esto imprimirá el texto del raise 'No se permiten edades negativas'

# Vamos a sacar la raiz cuadrada

def raiz(num):
  if num < 0:
    raise ValueError("El número no puede ser negativo")

  else:
    return math.sqrt(num)

try:
  print(raiz(-144))
except ValueError as NoRaizNegativa:
  print(NoRaizNegativa)