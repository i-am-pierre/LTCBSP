monthly_plan = int(input())
plan_length = int(input())
left_over = monthly_plan

for month in range(0,plan_length):
    current_month_consuption = int(input())
    data = monthly_plan + left_over - current_month_consuption
    if data < 0:
        data = 0
    else:
        left_over = data
print(f'{left_over}')
