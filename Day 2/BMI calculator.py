print("---Welcome to the basic BMI calculator---")

weight = float(input("What is your weight in kilogram? "))
print(weight, "kg")
height = float(input("And what is your height in meter? "))
print(height, "m")

BMI = weight/(height*height)

print("Your BMI is",BMI )