
# Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

'''
In Python, **kwargs allows a function to accept any number of keyword arguments (i.e., arguments passed as key=value). These are collected into a dictionary inside the function.
'''

def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(Name="Ravi", Branch="CSE")

print_kwargs(Name="Ravi")
print_kwargs(Branch="CSE")