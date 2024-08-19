# main
def not_unique(num):
    """
    num is an integer

    Return True if len(set(num)) is not equal to len(list(num)) else False
    """
    num_list = [int(i) for i in str(num)]
    num_set = set(num_list)
    return len(num_list) != len(num_set)

# Read input number
my_number = int(input())

# While next number is not not uniq, add one
my_number = my_number + 1

while not_unique(my_number):
    my_number = my_number + 1

print(my_number)
