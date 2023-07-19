p_value = int(input())
nb_people = int(input())
r_value = int(input())

day = 0
yesterday_num = nb_people

while nb_people <= p_value:
    nb_people = nb_people + yesterday_num * r_value
    day = day + 1
    yesterday_num = yesterday_num * r_value
#    print(f'Day: {day}, new cases: {yesterday_num}, Total Cases: {nb_people}')

print(f'{day}')
