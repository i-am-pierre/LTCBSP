nb_questions = int(input())
answers = input()

adrian, bruno, goran = 0, 0, 0

def adrian_answer(i: int):
    # A,B,C,A,B,C...
    if i % 3 == 0:
        return 'A'
    elif i % 3 == 1:
        return 'B'
    elif i % 3 == 2:
        return 'C'
    
def bruno_answer(i: int):
    # B,A,B,C,B,A,B,C...
    if i % 2 == 0:
        return 'B'
    else:
        if i % 4 == 1:
            return 'A'
        else: 
            return 'C'

def goran_answer(i: int):
    # C,C,A,A,B,B,C,C,A,A,B,B...
    if i % 6 == 0 or i % 6 == 1:
        return 'C'
    elif i % 6 == 2 or i % 6 == 3:
        return 'A'
    elif i % 6 == 4 or i % 6 == 5:
        return 'B'

def max_of_three(a:int, b:int, c:int):
    if a < b:
        if b < c:
            return c
        else: 
            return b
    else:
        if a < c:
            return c
        else:
            return a
        
for question in range(nb_questions):
    if adrian_answer(question) == answers[question]:
        adrian = adrian + 1
    if bruno_answer(question) == answers[question]:
        bruno = bruno + 1
    if goran_answer(question) == answers[question]:
        goran = goran + 1

win = max_of_three(adrian, bruno, goran)

print(f'{win}')
if adrian == win:
    print('Adrian')
if bruno == win:
    print('Bruno')
if goran == win:
    print('Goran')
