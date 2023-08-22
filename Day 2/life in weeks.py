age = int(input("Input your current age: "))

end = int(input("Please provide the end age: "))

day_age = age*365
week_age = age*52
month_age = age*12

day_end = end*365
week_end = end*52
month_end = end*12

day_left = day_end - day_age
week_left = week_end - week_age
month_left = month_end - month_age

print(f"You have {day_left} days, {week_left} weeks and {month_left} months left!")