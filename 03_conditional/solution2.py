# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter Your Age :"))
day="Wednesday"
price = 12 if age >= 18 else 8
if day == "Wednesday":
    #price=price-2
    price -= 2
print("Ticket price for you is : $",price)



#Output
'''Enter Your Age :11
Ticket price for you is : $6

Enter Your Age :17
Ticket price for you is : $6

Enter Your Age :18
Ticket price for you is : $10

Enter Your Age :56
Ticket price for you is : $10'''