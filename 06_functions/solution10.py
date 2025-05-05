# Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.


'''A recursive function is a function that calls itself to solve smaller instances of the same problem.
It must have a base case to stop the recursion and avoid infinite loops.'''

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

print(f"Factorial of {5}  =",factorial(5))