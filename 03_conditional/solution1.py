num = int(input("Enter a number :"))
if num<13:
    print("Child")
elif (num>=13 and num<=19):
    print("Teenanger")
elif (num>=20 and num<=59):
    print("Adult")
else:
    print("Senior")