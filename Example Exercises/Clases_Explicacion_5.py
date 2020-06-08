'''super( ) y isinstance( )'''

class Persona:

  def __init__(self, nombre, edad, ciudad_residencia):
    self.nombre = nombre
    self.edad = edad
    self.ciudad_residencia = ciudad_residencia

  def descripcion(self):
    print(f"Nombre: {self.nombre} - Edad: {self.edad} - Ciudad: {self.ciudad_residencia}")
    

class Empleado(Persona): # Un empleado también es una persona...pero tiene otras cualidades 
  def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
    #super().__init__("Sara Lopez", 25, "Medellín") # De esta forma le damos al Empleado un valor para los atributos en el constructor de la clase padre, en este caso Persona

    super().__init__(nombre_empleado, edad_empleado, residencia_empleado) # Podemos ahora usar las nuevas tres variables, las que tienen _empleado para pasar a la clase padre
    self.salario = salario
    self.antiguedad = antiguedad

  def descripcion(self):
    super().descripcion() # Aquí usamos el método de la clase padre

    print(f"Salario: {self.salario} - Antiguedad: {self.antiguedad}")

antonio = Persona('Antonio Ruiz', 22, 'Bogotá')
antonio.descripcion()

'''las siguientes dos instancias van a dar un error, porque si le pone dos atributos entra en conflicto con la herencia de Persona, y si le pone 3 entra en conflicto con los atributos de Empleado'''

#sara = Empleado(2_000_000, 8)
#sara = Empleado('Sara Lopez', 25, 'Medellin')
sara = Empleado(2_000_000, 20, "Sara Lopez", 45, 'Medellín') # Esto sirve porque usamos el método super( )
sara.descripcion() # Esto ejecuta primero la descripción en la clase Personas y luego la descripción de la clase Empleado

'''Ahora, hay que tener en cuenta la lógica. Una persona NO SIEMPRE es empleado, pero un empleado SIEMPRE es persona.

Este principio de sustitución debería usarse con cualquier clase para definir cuál es la superclase/clase padre'''

'''isinstance( )'''

#Esta función permite a python saber si una clase es instancia de otra dando True o False

print(isinstance(antonio, Empleado)) # False, porque antonio no es un empleado, sólo persona
print(isinstance(antonio, Persona)) # True, él es persona

print(isinstance(sara, Persona)) # True, ella es persona
print(isinstance(sara, Empleado)) # True, ella es empleada