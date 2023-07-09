numb_press = int(input())
my_string = 'A'
result_string = ''

def change_string(string:str):
    if string == 'A':
        return 'B'
    elif string == 'B':
        return 'BA'

for i in range(numb_press):
    result_string = ''
    for char in my_string:
        result_string += change_string(char)
        my_string = result_string

a_count = my_string.count('A')
b_count = my_string.count('B')

print(f"{a_count} {b_count}")
