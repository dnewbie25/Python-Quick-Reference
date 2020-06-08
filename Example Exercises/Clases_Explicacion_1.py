class Coche:
  # Creamos algunas propiedades básicas para cada instancia de la clase Coche (atributos)
  '''Estado Inicial'''
  # El estado inicial son estos 4 atributos básicos que se pueden poner dentro de un CONSTRUCTOR, el cual viene a ser __init__()
  def __init__(self): # Los constructores tienen dos __ al inicio y al final
    '''Si no queremos que las variables se modifiquen desde afuera de la clase, debemos encapsularlas, esto se hace mediante __ al inicio de los atributos'''
    self.__largo_chasis = 250
    self.__ancho_chasis = 120
    self.__ruedas = 4
    self.__en_marcha = True

  # Los métodos definen los comportamientos de la clase Coche (qué es capaz de hacer)
  def arrancar(self, arrancamos):
    # El self hace referencia al propio objeto perteneciente a la clase. A la instancia de la clase
    # self es el primer parámetro OBLIGATORIO
    self.__en_marcha == arrancamos

    if self.__en_marcha == True:
      # Si no se usa el self va a dar un 'Undefined variable Error'
      return 'El coche está en marcha'
    else:
      return 'El coche está parado'

  def estado(self):
    estado_coche = f"El coche tiene {self.__ruedas}. Tiene un largo de {self.__largo_chasis} cm y un ancho de {self.__ancho_chasis} cm"
    return estado_coche
    

# Un ejemplo de self, como en self.ruedas sería el equivalente a mi_coche.ruedas. La instancia antecede al atributo a buscar


'''Cómo se contruye un objeto o instancia'''

mi_coche = Coche() # Instanciar una clase

'''Cómo se llaman los atributos '''
# Si me interesa ver el largo del coche puedo usar nomenclatura del punto

'''Una vez se encapsula una variable ya no se puede acceder a ella desde fuera. Dar un Attribute Error. Sólo se pueden llamar los métodos dentro de la clase'''
#print(mi_coche.__largo_chasis) # Como largo_chasis no es una función sino una tributo no se usan paréntesis al final

#print(mi_coche.__ruedas) 

#print(mi_coche.__ancho_chasis)

'''Cómo se llaman los métodos'''

print(mi_coche.arrancar(False)) # Aquí sí se usan los paréntesis

print(mi_coche.estado())

'''Creando otra instancia'''

print("--------------Instancia 2--------------")

mi_coche2 = Coche()

mi_coche2.__largo_chasis = 122 # Esto cambiaría el valor del chasis. Si no queremos que se pueda hacer esto debemos encapsular largo_chasis poniendo __ al inicio dentro de la clase

print(mi_coche2.arrancar(False))

print(mi_coche2.estado())