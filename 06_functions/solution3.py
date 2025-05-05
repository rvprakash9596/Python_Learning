# Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
# Example : 
'''>>> 5*5
25
>>> "R"*5
'RRRRR' '''

def multiply(p1,p2):
    return p1*p2

print(multiply(5,7))
print(multiply("R",7))
print(multiply(3,"Ravi"))

