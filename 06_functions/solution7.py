# Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.
'''In Python, *args allows a function to accept a variable number of positional arguments. It collects extra positional arguments into a tuple.

def func_name(*args):
    # args is a tuple of all extra positional arguments
'''

def sum_all(*args): # we can write anythng in place of args
    print(args)
    return sum(args)
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,6))
print(sum_all(1,2,3,6,7,8,9))
