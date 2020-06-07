class Coche:
  # Creamos algunas propiedades básicas para cada instancia de la clase Coche (atributos)
  largo_chasis = 250
  ancho_chasis = 120
  ruedas = 4
  en_marcha = True

  # Los métodos definen los comportamientos de la clase Coche (qué es capaz de hacer)
  def arrancar(self):
    # El self hace referencia al propio objeto perteneciente a la clase. A la instancia de la clase
    # self es el primer parámetro OBLIGATORIO
    if self.en_marcha == False:
      self.en_marcha = True # Si no se usa el self va a dar un 'Undefined variable Error'
      return self.en_marcha
    else:
      return self.en_marcha

  def estado(self):
    if self.en_marcha == True:
      return 'En marcha'
    else:
      return 'Detenido'




'''Cómo se contruye un objeto o instancia'''

mi_coche = Coche() # Instanciar una clase

'''Cómo se llaman los atributos '''
# Si me interesa ver el largo del coche puedo usar nomenclatura del punto

print(mi_coche.largo_chasis) # Como largo_chasis no es una función sino una tributo no se usan paréntesis al final

print(mi_coche.ruedas)

print(mi_coche.ancho_chasis)

'''Cómo se llaman los métodos'''

print(mi_coche.arrancar()) # Aquí sí se usan los paréntesis

print(mi_coche.estado())