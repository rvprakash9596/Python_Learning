# Global variable : A variable has global scope if it is defined outside of any function or class. This means it can be accessed anywhere in the file, unless shadowed by a local variable with the same name.

x = 10  # Global variable
def show():
    print(x)  # Accessing global variable
show()  # Output: 10
