import math

cover = 5

height = int(input("Input height in meter: "))
width = int(input("Input width in meter: "))

def paint_cal(height, width, cover):
    area = height * width
    total = math.ceil(area/cover)
    print(f" Total {total} cans")

paint_cal(height, width, cover)