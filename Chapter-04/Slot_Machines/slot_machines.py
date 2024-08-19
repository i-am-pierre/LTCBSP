quarter_jar = int(input())
first_machine = int(input())
second_machine = int(input())
third_machine = int(input())

next_machine = 'first'
nb_play = 0

while quarter_jar >= 1:
    quarter_jar = quarter_jar - 1
    if next_machine == 'first':
        first_machine = first_machine + 1
        if first_machine % 35 == 0:
            quarter_jar = quarter_jar + 30
        next_machine = 'second'

    elif next_machine == 'second':
            second_machine = second_machine + 1
            if second_machine % 100 == 0:
                quarter_jar = quarter_jar + 60
            next_machine = 'third'

    elif next_machine == 'third':
            third_machine = third_machine + 1
            if third_machine % 10 == 0:
                quarter_jar = quarter_jar + 9
            next_machine = 'first'
    nb_play = nb_play + 1

print(f'Martha plays {nb_play} times before going broke.')
