def divide():

  try:
    num1 = float(input("Introduce el primero número: ")) 
    num2 = float(input("Introduce el segundo número: "))

    print("La división es " + str(num1 / num2))

# Los except se pueden declarar consecutivamente en caso de que puedan ocurrir muchos errores, como aquí donde puede dar error si se ingresan letras en vez de números o si se ingresa cero como denominador


  except ValueError: # Si no es un número

    print("El valor introducido es incorrecto")

  except ZeroDivisionError: # Si el denominador es cero
    print("No se puede dividir entre cero")
    

#También se puede poner except solito para que capture todas las excepciones, pero no ayuda al #usuario a saber qué pasó pues no le darías ningún mensaje específico

 # except:
  #  print("El valor es incorrecto o el denominador es cero")
  finally:
    print("Cálculo finalizado")

  # Si quisiéramos un código que se ejecute siempre sin importar si falla o no, podríamos usar el finally o dejar sólo el print

  

divide()