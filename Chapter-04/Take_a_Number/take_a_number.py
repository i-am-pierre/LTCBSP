queue_number = int(input())

action = input()
ticket_taken = 0
late_student = 0

while action != 'EOF':
    if action == 'TAKE':
        queue_number = queue_number + 1
        ticket_taken = ticket_taken + 1
        if queue_number > 999:
            queue_number = 1
    if action == 'SERVE':
        late_student = late_student + 1
        ticket_taken = ticket_taken - 1
    if action == "CLOSE":
        print(f'{late_student + ticket_taken} {ticket_taken} {queue_number}')
        late_student = 0
        ticket_taken = 0

    action = input()
