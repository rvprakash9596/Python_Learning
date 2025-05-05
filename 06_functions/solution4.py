# Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math

def circle_stats(r):
    area = math.pi*r**2
    circumference = 2*math.pi*r
    return area , circumference
r = float(input("Enter the radius of the circle: "))
a,c = circle_stats(r)
print(f"Area = {a:.2f}")
print(f"Circumference = {c:.2f}")