def cal_counting (burger:int, drink:int, side:int, dessert:int):
    # Result adds all calorie options
    result = burger + drink + side + dessert    
    return result

input_burger = int(input())
if input_burger == 1:
    burger_cal = 461
elif input_burger == 2:
    burger_cal = 431
elif input_burger == 3:
    burger_cal = 420
else: 
    burger_cal = 0

input_side = int(input())
if input_side == 1:
    side_cal = 100
elif input_side == 2:
    side_cal = 57
elif input_side == 3:
    side_cal = 70
else:
    side_cal = 0

input_drink = int(input())
if input_drink == 1:
    drink_cal = 130
elif input_drink == 2:
    drink_cal = 160
elif input_drink == 3:
    drink_cal = 118
else: 
    drink_cal = 0

input_dessert = int(input())
if input_dessert == 1:
    dessert_cal = 167
elif input_dessert == 2:
    dessert_cal = 266
elif input_dessert == 3:
    dessert_cal = 75
else:
    dessert_cal = 0

total_cal = cal_counting (burger_cal, drink_cal, side_cal, dessert_cal)

print(f"Your total Calorie count is {total_cal}.")
