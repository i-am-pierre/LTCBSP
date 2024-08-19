p_litre = int(input())
b_cap = int(input())
d_price = int(input())

def day_output (p, b, d):
    nb_cap = p // b
    left_over = p % b
    output = ( nb_cap * d ) + left_over
    return output

print(f"{day_output(p_litre, b_cap, d_price)}")
