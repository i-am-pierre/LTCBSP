nb_of_questions = int(input())
ref_choice = ''
points = 0

for question_nb in range(nb_of_questions):
    question = input()
    ref_choice = ref_choice + question

# print(f'{ref_choice}')

for response_nb in range(nb_of_questions):
     response = input()
     if response == ref_choice[response_nb]:
         points = points + 1
print(f'{points}')
