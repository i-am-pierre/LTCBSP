def special_date (month: int, day:int):
    # Function return Before, After, or Special depending on logic
    if (month == 2) and (day == 18):
        return "Special"
    elif (month < 2) or (month == 2 and day < 18):
        return "Before"
    else:
        return "After"
    
my_month = int(input())
my_day = int(input())
my_answer = special_date(my_month, my_day)

print(f"{my_answer}")
