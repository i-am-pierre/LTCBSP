def is_telemarketer (first:int, second:int, third:int, forth:int):
    # function returning string based on logic
    if (first == 8 or first == 9) and (forth == 8 or forth == 9) and (second == third):
        return "ignore"
    else:
        return "answer"

first_digit = int(input())
second_digit = int(input())
third_digit = int(input())
fourth_digit = int(input())

answer = is_telemarketer(first_digit, second_digit, third_digit, fourth_digit)
print(f"{answer}")
