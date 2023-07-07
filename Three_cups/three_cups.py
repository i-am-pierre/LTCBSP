pattern = input()
ball = '1'

for swap_type in pattern:
    if swap_type == 'A':
        if ball == '1':
             ball = '2'
        elif ball == '2':
             ball = '1'
    if swap_type == 'B':
         if ball == '2':
             ball = '3'
         elif ball == '3':
              ball = '2'
    if swap_type == 'C':
         if ball == '3':
              ball = '1'
         elif ball == '1':
              ball = '3'

print(ball)
