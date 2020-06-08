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
  # ¿Qué puede hacer una moto que no pueda hacer un autobus o una lancha?

  