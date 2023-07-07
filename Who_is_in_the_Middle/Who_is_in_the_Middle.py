def my_middle (a:int, b:int, c:int):
    if a <= b:
        if a >= c:
            return a
        elif b <= c:
            return b
        else:
            return c
    else:
        if a <= c:
            return a
        elif b <= c:
            return c
        else:
            return b


a = int(input())
b = int(input())
c = int(input())

my_answer = my_middle(a, b, c)

print(f'{my_answer}')
