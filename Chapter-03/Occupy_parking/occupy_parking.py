car_park_space = int(input())
yesterday_setup = input()
today_setup = input()

def occupied_both_days(y:str, t:str):
    # TBD
    return  (y == 'C') and (t == 'C')

def count_commun_space(yesterday:str, today:str, car_space:int):
    count = 0
    for car in range (0,car_space):
        if occupied_both_days(yesterday[car], today[car]):
            count = count + 1
    return count

result = count_commun_space(yesterday_setup, today_setup, car_park_space)

print(f'{result}')
