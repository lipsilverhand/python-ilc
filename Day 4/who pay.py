import random

names_str = input("Input the names without separated commas:") #input names: Lip Phuong Duy Tung
names = names_str.split() #make the lists of the input: "Lip" "Phuong" "Duy" "Tung"

who_pay = random.choice(names) # Random pick one of the list of "names"

print(who_pay + " is going to pay the bill.")
