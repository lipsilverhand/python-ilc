print("---Welcome to Washington fair ticket box---")

age = int(input("What is your age? "))

if age>=18 and age<65:
    print("You are adult and you have to pay $25/ticket.")

elif age>=10 and age<18:
    print("You are teen and you have to pay $18/ticket.")
else:
    print("You are kid or senior adult, congrats you just got free ticket! ")

