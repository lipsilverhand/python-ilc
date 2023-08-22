print("---Welcome To The Bill Calculator!---")

bill= float(input("How much for total bill? $"))
people= int(input("How many people are there? "))
tip= int(input("How much you give the tip in percentage? "))
tipPercent = tip/100 * bill
tax_WA= 6.5/100 * bill

totalBill = bill + tax_WA + tip
print(f"Total bill is: {totalBill}$")

seperateBill= totalBill/people
print(f"Each person needs to pay {seperateBill}$")