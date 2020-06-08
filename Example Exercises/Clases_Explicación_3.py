'''-----------------HERENCIA------------------'''

# Se trata de trasladar el comportamiento de los objetos en la vida real a la programación

'''Jerarquía de Herencia

Abuelo: tiene una casa
  Padre: tiene un carro
    Hijo1 tiene una moto
    Hijo2 tiene una bicicleta
    Hijo3 no tiene nada
    
Si el abuelo fallece el padre de los hijos la hereda. Quedando el padre con carro y casa.
Si el padre fallece sus bienes pasan al hijo predilecto, digamos el Hijo2. Quien ahora tiene carro, casa y bicicleta.

En programación sería

Clase 1: --> Clase padre o superclase

  Clase 2: --> Superclase de clase 3,4 y 5 y subclase de Clase 1

    Clase 3: Todas estas tres son subclases de la clase 2 y a su vez subclases de la clase 1
    Clase 4:
    Clase 5:

La herencia sirve para crear objetos similares, ejemplo carro, autobuses, motocicletas, tractores, camiones de carga.

****  Debes pensar:

¿qué características tienen en común? --> Una marca y un modelo

¿qué comportamientos tienen en común? --> arrancar, acelerar, frenar, girar

Generalmente tienen objetivos diferentes (autobus lleva pasajeros, una moto una sola persona o domicilios)

Si no hubiera herencia debería crear los objetos uno en uno y desde cero cada uno.

****  La herencia permite coger todos los comportamientos y características en común y englobarlos en una superclase.

'''


# Un ejemplo práctico para los vehículos

class Vehiculos:

  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
    # Ahora agregamos 3 características más
    self.enmarcha = False # comienza detenido en todo, no frena, acelera ni arranca
    self.acelerar = False
    self.frenar = False
  
  '''Definimos los comportamientos. Estos activarían los atributos que definimos anteriormente'''
  def arrancar(self):
    self.enmarcha = True

  def aceleracion(self):
    self.acelerar = True

  def frena(self):
    self.frenar = True

  def estado(self):
    print(f"\nMarca: {self.marca} - Modelo {self.modelo}")
    print(f"En Marcha: {self.enmarcha} - Acelerando: {self.acelerar} - Frenando: {self.frenar}")

# Cómo se crea un objeto que herede de la clase vehículos

class Moto(Vehiculos): # Se pone como argumento el nombre de la clase que queremos que herede
  pass # Para que Python entiendo que no vamos a agregar nada por ahora, pero que no envíe un error

mi_moto = Moto('Kawazaki', 'Hayabusa')

mi_moto.estado() # Saldría con todo False

mi_moto.aceleracion()
mi_moto.arrancar()

mi_moto.estado() # Ahora está en marcha y acelerando

