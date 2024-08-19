bcases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

nb_removed = int(input())

for i in range(nb_removed):
    opened_case = int(input()) - 1
    bcases[opened_case] = 0

banker_offer = int(input())

# print(bcases)

total, my_average = 0, 0

for bcase in bcases:
    total = total + bcase

# print(f'Total: {total}')
my_average = total / ((len(bcases)) - nb_removed)

# print(f'My avg: {my_average}')
# print(f'Offer: {banker_offer}')

if my_average < banker_offer:
    print('deal')
else:
    print('no deal')
