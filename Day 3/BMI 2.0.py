print("---Welcome to the basic BMI calculator ver 2.0---")

weight = float(input("What is your weight in kilogram? "))
print(weight, "kg")
height = float(input("And what is your height in meter? "))
print(height, "m")

BMI = weight/(height*height)

print("Your BMI is",BMI )

if BMI<18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI>18.5 and BMI<25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI>25 and BMI<30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI>30 and BMI<35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")




