# Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number  = int(input("Enter Value between 1 and 10 :"))
    if 1<= number<=10:
        print("Welcome")
        break
    else:
        print("Invalid Number , Re-Start")