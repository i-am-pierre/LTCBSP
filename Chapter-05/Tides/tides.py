def is_stricly_increasing(l:list):
    #test if the list of int is stricly increasing
    current = l[0]
    if len(l) == 1:
        return True
    for element in l[1:]:
        if current < element:
            return is_stricly_increasing(l[1:])
        else:
            return False
    return True

n = int(input())

# Getting second line of data into a list of integers
measure_str = input()
measure_list = list(map(int, measure_str.split()))

# Finding min and max element
min_measure = min(measure_list)
max_measure = max(measure_list)

# Finding index of the min and max
min_index = measure_list.index(min_measure)
max_index = measure_list.index(max_measure)

if min_index > max_index:
    print('unknown')
else:    
    # test for valid measurment and return tide
    if is_stricly_increasing(measure_list[min_index:max_index]):
        tide = max_measure - min_measure
        print(tide)
    else:
        print('unknown')
