class Car:
    '''Create a class Car'''

    def __init__(self, make, model, year):
        '''Initialize the attributes'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 # This attribute will change with time, but it's not required for the __ini__() to execute. The 0 is is default value

    def get_descriptive_name(self):
        '''We want to return a string with no None value returned at the end'''
        description = f"{self.year}, {self.make}, {self.model}"
        return description.title()

    def read_odometer(self):
        '''Returns the amount of miles the odometer shows'''
        print(f"This car has {self.odometer} miles on it")

    def update_odometer(self, mileage):
        '''Modify the odometer's value to the value of the mileage variable'''
        # self.odometer = mileage this would be the basic way. Now, let's define a way to not rolling back the odometer. You shouldn't be able to put the odometer in zero i real life.

        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back the odometer!!")

    def increment_odometer(self, miles):
        '''Add a specific amount to the odometer'''
        self.odometer += miles # Add the miles to our initial odometer = 0

'''Create en Electric Car class'''

class Electric_Car(Car):
    def __init__(self, make, model, year):
      '''Initialize the attributes of the parent class, Car'''
      super().__init__(make, model, year)
      self.battery_size = 75 # We initialize the attributes of the parent class but we also add one attribute exlucive to Electric_Car

    def describe_battery(self):
      print(f"This car a {self.battery_size}-kWh battery")

my_tesla = Electric_Car('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
print(my_tesla.battery_size)
my_tesla.describe_battery()