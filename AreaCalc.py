import math

def paint_calc(height, width, cover):
    num_of_cans = (height * width) / cover
    rounded_cans = math.ceil(num_of_cans)
    print(f"You'll need {rounded_cans} cans of paint")


 
user_h = int(input("Height of wall: "))
user_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=user_h, width=user_w, cover=coverage)

