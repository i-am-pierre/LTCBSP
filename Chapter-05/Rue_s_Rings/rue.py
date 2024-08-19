MAX = 70000

for dataset in range(10):
    minimum = MAX
    list_of_min = []
    nb_of_route = int(input())

    for i in range(nb_of_route):
        line = list(map(int, input().split()))
        route_id = line[0]
        d_list = line[2:]
        route_min = min(d_list)

        if route_min < minimum:
            list_of_min = [route_id]
            minimum = route_min
        elif route_min == minimum:
            list_of_min = list_of_min + [route_id]
    
    list_of_min.sort()
    output = ','.join(map(str, list_of_min))
                      
    print(f"{minimum} {{{output}}}")
