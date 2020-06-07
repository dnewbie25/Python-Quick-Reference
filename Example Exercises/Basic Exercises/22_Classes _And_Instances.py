class Car:
    '''Create a class Car'''

    def __init__(self, make, model, year):
        '''Initialize the attributes'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 # This attribute will change with time, but it's not required for the __ini__() to execute

    def get_descriptive_name(self):
        '''We want to return a string with no None value returned at the end'''
        description = f"{self.year}, {self.make}, {self.model}"
        return description.title()

    def read_odometer(self):
        '''Returns the amount of miles the odometer shows'''
        print(f"This car has {self.odometer} miles on it")


# We create an instance

my_car = Car('Mazda','3 piCkUp', '2018')
print(my_car.get_descriptive_name())
my_car.read_odometer() # We don't use print() here because otherwise it would print None. None is the return value from the function read_odometer(). You can just create a variable to use print() but I decided not doing so this time