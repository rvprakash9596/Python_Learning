# Problem: Check if a number is prime
number = int(input("Enter number to check Prime : "))

is_prime = True

if number>1:
    for i in range(2,number):
        if(number%i)==0:
            is_prime = False
            break
else:
    is_prime = False

print(is_prime)