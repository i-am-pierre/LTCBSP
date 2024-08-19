for dataset in range(10):
    nt_str = input()
    nt_list = nt_str.split()

    t_value = int(nt_list[0])
    n_value = int(nt_list[1])

    delay_day = 0
    for day in range(n_value):
        action = input()
        if action == 'E' and delay_day > 0:
            delay_day = delay_day -1
        elif action == 'B':
            delay_day = delay_day + t_value - 1

    print(delay_day)
