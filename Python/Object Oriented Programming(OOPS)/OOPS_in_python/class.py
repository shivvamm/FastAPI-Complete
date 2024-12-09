class Car:
    # Class variable that is shared by all the instances of the class 
    # Defined after the class and before the constructor
    total_car = 0
    # Instance variables owned by every instance will be different  
    # Define within the method 
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car += 1
    
    def get_brand(self):
        return self.__brand+"!"
    
        # Polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"
    
    # Self is not requred because it is a static method 
    # objects cannot access static methods
    @staticmethod
    def general_des():
        return "Cars are means of transport and amazing also"

    # Property makes sure that we cannot change the value after intialiation 
    @property
    def model(self):
        return self.__model

class EletricCar(Car):
    def __init__(self,brand,model,battery_size):
        # Available for the class and encapsulated form others  using __
        super().__init__(brand,model)
        self.battery_size= battery_size

    #  Polymorphism
    def fuel_type(self):
        return "Eletric Charge"


my_car = Car("Toyota","Camry")
# print(my_car.brand)
new_car = EletricCar("Tesla","Model S", 100)
print(new_car.battery_size) 
# print(new_car.__brand)
print(new_car.get_brand())
print(my_car.fuel_type())
print(new_car.fuel_type())  
print(my_car.total_car)
test = Car("test","test")
# print(test.total_car)

# Direct access makes a new object 
print(Car.total_car)
print(Car.general_des())
# print(my_car.general_des())
# Cannot acces
# my_car.model = "Corolla"
# read only to access 
print(my_car.model)


# Isinstance to check if that the object is an instance of the class Car and Electric car
print(isinstance(my_car,Car))
print(isinstance(new_car,Car))


class Battery:
    def battery_info(self):
        return "This is a battery"
    

# Multiple inheritence

class Engine:
    def engine_info(self):
        return "This is an engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())