lines_of_text = int(input())
t_nb = 0
s_nb = 0

def lang_check(t:int, s:int):
    if t > s:
        return 'English'
    else:
        return 'French'

for line in range(lines_of_text):
    sample_line = input()
    for char in sample_line.lower():
        if char == 's':
            s_nb = s_nb +1
        elif char == 't':
            t_nb = t_nb +1

result = lang_check(t_nb, s_nb)
print(f'{result}')
