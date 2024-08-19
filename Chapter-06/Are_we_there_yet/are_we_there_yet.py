from icecream import ic

def calculate_city(city, lst):
    """
    city is the city index, lst is a list of distance.

    Return a list of 5 distances from the city index to the 4 other cities.
    """
    one_two = lst[0]
    two_three = lst[1]
    three_four = lst[2]
    four_five = lst[3]

    if city == 0:
        return list_of_dist(0, one_two, one_two + two_three, one_two + two_three + three_four, one_two + two_three + three_four + four_five)
    elif city == 1:
        return list_of_dist(one_two, 0, two_three, two_three + three_four, two_three + three_four + four_five)
    elif city == 2:
        return list_of_dist(one_two + two_three, two_three, 0, three_four, three_four + four_five)
    elif city == 3:
        return list_of_dist(one_two + two_three + three_four,  two_three + three_four, three_four, 0, four_five)
    elif city == 4:
        return list_of_dist(one_two + two_three + three_four + four_five, two_three + three_four + four_five, three_four + four_five, four_five, 0)

def list_of_dist(a, b, c, d, e):
    """
    a, b, c, d, e are 5 integer

    Return a list of the 5 integer
    """
    result = []
    result.append(a)
    result.append(b)
    result.append(c)
    result.append(d)
    result.append(e)
    return result

# Main

# Read inputs
lst_of_dist = list(map(int, input().split()))

# Calculate distance between current city to all 4 other cities
for i in range(5):
    line = calculate_city(i, lst_of_dist)
    print(*line)
