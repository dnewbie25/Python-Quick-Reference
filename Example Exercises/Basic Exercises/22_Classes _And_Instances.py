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
    


# We create an instance

my_car = Car('Mazda','3 piCkUp', '2018')
print(my_car.get_descriptive_name())
my_car.read_odometer() # We don't use print() here because otherwise it would print None. None is the return value from the function read_odometer(). You can just create a variable to use print() but I decided not doing so this time

print("\n\n--------------------Modifying Attributes Directly:-----------------------------\n\n")

'''Modifying Attributes:

Modifying an Attribute’s Value Directly
'''
my_new_car = Car('audi', 'a4', 2019)
my_new_car.odometer = 250 # We change the odometer value for this car to 250
my_new_car.read_odometer()


print("\n\n----------------------Modifying an Attribute’s Value Through a Method:-----------------------------\n\n")

# Here you create a method to modify the odometer inside the class Car. Take a look above to update_odometer()

my_new_car_2 = Car('renault', 'sandero,', 2005)
my_new_car_2.update_odometer(500)
my_new_car_2.read_odometer()

print("\n\n----------------------Incrementing an Attribute’s Value Through a Method:------------------------------\n\n")

# Say we want to add some mileage to our car from the time we buy it to the time we register it (yes, you drive you car before registering it in most places)

# We add a method called increment_odometer() in class Car, take a look above

my_new_car_3 = Car('chevrolet', 'blazer', 2001)

my_new_car_3.update_odometer(1500) # This car was used before, so it has 1500 miles
my_new_car_3.read_odometer()

my_new_car_3.increment_odometer(150) # We buy it and drive 150 miles more to register it 
my_new_car_3.read_odometer()