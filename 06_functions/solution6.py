# Lambda Function
# Problem: Create a lambda function to compute the cube of a number.

'''A lambda function in Python is a small, anonymous function defined using the lambda keyword. It's often used when you need a simple function for a short period and don't want to formally define it with def.'''

cube = lambda x : x**3
print(cube(3))


#using function
def cube(num):
    return num**3
print("Cube =",cube(5))