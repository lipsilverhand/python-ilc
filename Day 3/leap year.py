print("---Leap year or Not leap year---")

year = int(input("Inout the year: "))

if (year % 4 != 0 ):
    print("Not leap year!")

elif (year % 4 == 0 & year % 100 == 0 & year % 400 == 0 | year % 100 != 0):
    print("Leap year")
else: 
    print("Not leap year")
    