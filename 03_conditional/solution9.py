#  Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = int(input("Enter Year to check Leap : "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
    print(year," is Leap Year")
else:
    print(year , " is not Leap Year")