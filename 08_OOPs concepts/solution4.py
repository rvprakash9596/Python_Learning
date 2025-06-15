#Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

#Encapsulation is the process of wrapping data (variables) and the methods (functions) that operate on that data into a single unit, i.e., a class. It also restricts direct access to some of the object's components, which is a means of data hiding.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand + "!"

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

# Example usage
my_tesla = ElectricCar("Tesla", "Model S", "95kwh")
print(my_tesla.brand)
print(my_tesla.get_brand())
