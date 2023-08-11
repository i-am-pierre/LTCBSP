# 10 set of data
for dataset in range(10):
    # Getting first line of data n,m,d
    nmd_str = input()
    nmd_list = nmd_str.split()

    n_value = int(nmd_list[0])
    m_value = int(nmd_list[1])
    d_value = int(nmd_list[2])

    # Getting second line of data into a list
    event_str = input()
    event_list = list(map(int, event_str.split()))
    # print(event_list)

    clean_shirt = n_value
    wash = 0

    # go through everyday and test if he needs to do a wash
    for day in range(1,d_value + 1):
        # Test for a shirt for tomorrow, if so do a wash and reset clean_shirt
        if clean_shirt == 0:
            wash = wash + 1
            clean_shirt = n_value
        # Test if the day has partr of the event list    
        if day in event_list:
            # Can have multiple event a day, count event in event_list
            added_shirt = event_list.count(day)
            clean_shirt = clean_shirt + added_shirt
            # Update n_value
            n_value = n_value + added_shirt
        # End of the day, current shirt is now dirty
        clean_shirt = clean_shirt - 1
    # print(f'{wash} : {listofdays}')
    print(wash)
