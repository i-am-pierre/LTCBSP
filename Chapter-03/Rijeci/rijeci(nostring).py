a_count = 0
b_count = 1

for i in range(int(input()) - 1):
    prev_a_count = a_count
    prev_b_count = b_count
    b_count = prev_a_count + prev_b_count
    a_count = prev_b_count

print(f'{a_count} {b_count}')
