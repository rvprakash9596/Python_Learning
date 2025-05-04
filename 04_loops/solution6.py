#  Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

number = int(input("Enter Number to print factorial of this : "))

original_num = number
factorial = 1

while number > 0:
    factorial = factorial*number
    number -=1
print(f"The factorial of {original_num} is = ",factorial)
