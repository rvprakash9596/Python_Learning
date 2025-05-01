# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

num = int(input("Enter a number :"))
if num<13:
    print("Child")
elif (num>=13 and num<=19):
    print("Teenanger")
elif (num>=20 and num<=59):
    print("Adult")
else:
    print("Senior")