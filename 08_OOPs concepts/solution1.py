# Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self,brand,model): # init is a constructor
        # brand = None
        # model = None
        self.brand = brand
        self.model = model


obj1 = Car("Toyota","Corolla")
print(obj1.brand)
print(obj1.model)

obj2 = Car("Suzuki","Dzire")
print(obj2.brand)
print(obj2.model)
