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
  hacer_caballito = "" # Creamos algo que otras instancias de vehículos no pueden hacer

  def caballito(self):
    self.hacer_caballito = "Voy haciendo un caballito"

    # Si queremos que el metodo estado() indique si está o no haciendo un caballito NO PODEMOS modificar el método en la clase Vehiculos, porque no todos los vehiculos pueden hacer eso.
    
    '''Debemos crear un método estado() sólo para la clase Moto'''

  def estado(self): # Así se llame igual, el hecho de declararlo en la clase Moto hace que se use este en lugar del estado() en la clase Vehiculos
    print(f"\nMarca: {self.marca} - Modelo {self.modelo}")
    print(f"En Marcha: {self.enmarcha} - Acelerando: {self.acelerar} - Frenando: {self.frenar}\n{self.hacer_caballito}")



mi_moto = Moto('Suzuki', 'AX4')

mi_moto.estado() # Aquí todo está False

mi_moto.arrancar()
mi_moto.aceleracion()

mi_moto.estado() # Aquí arranca y acelera

mi_moto.caballito()

mi_moto.estado() # Aquí dice que va haciendo un caballito

'''Creamos otra instancia que herede de vehículos'''

class Furgoneta(Vehiculos): # Esta no hereda nada de la clase Moto...por ejemplo una furgoneta no puede hacer caballitos
  # Qué tiene una furgoneta en comparación a una moto? Puede llevar más carga
  def carga(self, cargar):
    self.cargar = cargar

    if self.cargar == True:
      return 'La furgoneta está cargada'
    else:
      return 'La furgoneta no lleva ninguna carga'

mi_furgoneta = Furgoneta('Renault', 'Pick up') # Así la clase Furgoneta no tenga constructor, debido a que está heredando de Vehiculos debemos pasarle dos argumentos

mi_furgoneta.estado()
print(mi_furgoneta.carga(True))

'''Ahora, digamos que queremos agregar vehículos eléctricos.
Aunque estos arrancan, frenan y aceleran, poseen ciertas características que los vuelven una clase aparte:
'''

class V_Electricos(Vehiculos): # Como ven esta no hereda nada. Es una clase independiente
  # Los eléctricos sabemos que no usan gasolina entonces debemos inicializar un constructor
  def __init__(self, marca, modelo):

    super().__init__(marca, modelo) # De esta forma puede recibir los argumentos de la clase Vehiculos

    self.autonomia = 100 # Batería da 100 Km de recorrido

  #Debemos conocer la carga de la batería
  def carga_energia(self):
    self.cargando = True # El vehículo está cargando si llamamos este método

'''Ahora digamos que queremos crear una bicicleta eléctrica. Esta puede hacer todo lo que hace la clase Vehículos pero ademá tiene características y métodos de la clase V_Electricos

Esto se llama Herencia Múltiple:

'''

class Bici_Electrica(V_Electricos, Vehiculos): # Le decimos que hereda de dos clases todos los métodos y atributos
  pass # Por ahora estará vacio

mi_bici = Bici_Electrica('Canondale', 'GTX125') 
'''Como hereda de dos, hay dos constructores. En este caso se da preferencia a la primera clase que indica entre los paréntesis de Bici_Electrica, en este caso usará el constructor de V_Electricos, que en este caso no tiene argumentos'''

'''funciones super() y isinstance()'''

# Si quisiéramos usar el constructor de Vehiculos en las bicicletas podríamos o crear los parámetros en Bici_Electrica, que no es lo ideal o usar un método:

'''super() --> El cual sirve para llamar al constructor de la clase Padre'''

#Ahora sí ya se usó super( ) en las bicicletas
mi_bici.estado()


