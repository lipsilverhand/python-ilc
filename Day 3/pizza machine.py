print("Welcome To The Pizza Vending Machine")

print("------------------------------------------")

size= input("Please pick your size (S, M, L)")


if size=="S":
    print("Small pizza")
    price=15
elif size=="M":
    print("M")
    price=20
else:
    print("Large pizza")
    price=25

pep = input("Would you like to add pepperoni? (Y/N)")

if pep=="Y":
    print("I would like to add pepperoni!")
    if size=="S":
        print("Add pepperoni to small size for $3")
        price = price + 3
    else:
        print("Ad  pepperoni to medium/large size for $5")
        price = price + 5
else: 
    print("No, thank you!")
    

cheese = input("Would you like to add-on cheese? (Y/N)")

if cheese=="Y":
    print("Yes please")
    price = price + 2
else:
    print("No, thank you!")

total = price

print("----------------------------------------")
print(f"You total is {total}$, your order will be ready soon, thank you for making a purchase!")
print("Have a good one!")
