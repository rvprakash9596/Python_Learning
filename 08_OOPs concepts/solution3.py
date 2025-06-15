# Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

# Base class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.make} {self.model} {self.year}")

# Derived class
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)  # Call the constructor of the base class
        self.battery_size = battery_size

    def display_info(self):
        super().display_info()
        print(f"Battery Size: {self.battery_size} kWh")

# Example usage
my_tesla = ElectricCar("Tesla", "Model S", 2024, 100)
my_suzuki = ElectricCar("Dzire", "VXI", 2024, 120)
my_tesla.display_info()
my_suzuki.display_info()
