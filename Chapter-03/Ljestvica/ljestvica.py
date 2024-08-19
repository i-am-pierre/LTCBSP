composition = input()

C_major_count = 0
A_minor_count = 0
current_measure = ''

def is_C_major(note:str):
    if note[0] == 'C' or note[0] == 'F' or note[0] == 'G':
        return True
    else:
        return False
    
def is_A_minor(note:str):
    if note[0] == 'A' or note[0] == 'D' or note[0] == 'E':
        return True
    else:
        return False

# Parse string check for measure
    # Pick the first chord of each mesasure and increment counter
for char in composition:
    if char == '|':
        if is_C_major(current_measure):
            C_major_count = C_major_count + 1
        elif is_A_minor(current_measure):
            A_minor_count = A_minor_count + 1
        current_measure = '' 
    else:
        current_measure = current_measure + char

if is_C_major(current_measure):
    C_major_count = C_major_count + 1
elif is_A_minor(current_measure):
    A_minor_count = A_minor_count + 1

# Find dominant tone 
if A_minor_count == C_major_count:
    if is_C_major(current_measure[-1]):
        C_major_count = C_major_count + 1
    elif is_A_minor(current_measure[-1]):
        A_minor_count = A_minor_count + 1

if A_minor_count > C_major_count:
    print('A-mol')
else:
    print('C-dur')
