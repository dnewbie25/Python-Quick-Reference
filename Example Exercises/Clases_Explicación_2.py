'''-------------------ENCAPSULACIÓN---------------'''

class Coche:
  '''Estado Inicial'''
  def __init__(self): 
    '''Si no queremos que las variables se modifiquen desde afuera de la clase, debemos encapsularlas, esto se hace mediante __ al inicio de los atributos'''
    self.__largo_chasis = 250
    self.__ancho_chasis = 120
    self.__ruedas = 4
    self.__en_marcha = True

  def arrancar(self, arrancamos):
    self.__en_marcha = arrancamos

    if self.__en_marcha == True: # Si se enciende el auto se debe ejecutar el chequeo
      chequeo = self.__chequeo_interno() # Se usa la función chequeo_interno()
    
    if self.__en_marcha == True and chequeo == True: # Si ya está encendido pues no puede volver a encenderse. Además si está encendido y el chequeo está True el auto está en movimiento
      return 'El coche está en marcha'
    elif self.__en_marcha == True and chequeo == False: # Si el chequeo falló al encender el auto. Recordar que no es posible hacer el chequeo automático con el auto apagado
      return 'Algo salió mal. No se puede arrancar'
    else: # Si todo está False significa que el auto está parado
      return 'El auto está detenido'

  def estado(self):
    estado_coche = f"El coche tiene {self.__ruedas}. Tiene un largo de {self.__largo_chasis} cm y un ancho de {self.__ancho_chasis} cm"
    return estado_coche

  def __chequeo_interno(self): # Como los autos reales, al encenderlo indica si tiene gasolina, aceite, puertas cerradas y eso

    # El chequeo debería hacerse apenas se enciende el auto, por lo tanto debería ejecutarse chequeo_interno() en el método arrancar()
    print("Realizando chequeo interno")

    self.gasolina = 'Ok'
    self.aceite = 'Ok'
    self.puertas = 'Cerradas'

    if self.gasolina == 'Ok' and self.aceite == 'Ok' and self.puertas == 'Cerradas':
      return True
    else:
      return False

'''La encapsulación se trata de poner __ al inicio de la variable para que no se pueda acceder a ella desde fuera'''
print("\n\n------------Primer coche----------\n\n")
mi_coche = Coche()

print(mi_coche.arrancar(True)) # Se dice que arranque
print(mi_coche.__chequeo_interno())
print("\n\n------------Segundo coche----------\n\n")

mi_coche_2 = Coche()

print(mi_coche_2.arrancar(False))
#print(mi_coche_2.__chequeo_interno()) 
''' Este método se puede acceder por fuera, incluso si el auto está apagado y eso no tiene sentido. Debemos encapsularlo, ahora con los dos __ no se puede acceder a él'''