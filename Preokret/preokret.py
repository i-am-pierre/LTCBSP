HALF_TIME = 1440

team_a_score = int(input())
team_a_sheets = []

ht_pts = 0
for time in range(team_a_score):
    time_stamp = [int(input())]
    if time_stamp[0] <= HALF_TIME:
        ht_pts = ht_pts + 1
    team_a_sheets = team_a_sheets + time_stamp

team_b_score = int(input())
team_b_sheets = []
for time in range(team_b_score):
    time_stamp = [int(input())]
    if time_stamp[0] <= HALF_TIME:
        ht_pts = ht_pts + 1
    team_b_sheets = team_b_sheets + time_stamp

# print(team_a_sheets)
# print(team_b_sheets)

timeline = []
for second in range(1, HALF_TIME * 2 + 1):
    if second in team_a_sheets:
        timeline = timeline + ['a']
    elif second in team_b_sheets:
        timeline = timeline + ['b']   

# print(timeline)

lead = timeline[0]
turnarounds = 0
a,b = 0,0

for event in timeline:
    if event == 'a':
        a = a + 1
    else:
        b = b + 1
    
    if a > b and lead == 'b':
        turnarounds = turnarounds + 1
        lead = 'a'
    elif b > a and lead == 'a':
        turnarounds = turnarounds + 1
        lead = 'b'
#    print(f'{a} - {b}')

print(ht_pts)
print(turnarounds)
