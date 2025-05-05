# Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fulldetails(self):
        return f"{self.brand} {self.model}"

obj1 = Car("Toyota","Corolla")
print(obj1.brand)
print(obj1.model)
print(obj1.fulldetails())
print(obj1.fulldetails())
print(obj1.fulldetails())

