temp_c = int(input())

def conv_celsius_to_fahreneit(temp_cel):
    temp_far = (temp_c * 9) / 5 + 32
    return temp_far

print(f"{conv_celsius_to_fahreneit(temp_c)}")
