class Employee:
  def __init__(self, firstName, lastName, annualSalary):
    """Define the three main attributes of an employee"""
    self.firstName = firstName
    self.lastName = lastName
    self.annualSalary = annualSalary

  def give_raise(self, raiseAmount = 5000):
    return self.annualSalary + raiseAmount

employee1 = Employee('Dani', 'Montoya', 25000)
print(employee1.give_raise())

