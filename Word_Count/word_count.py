my_input = input()

def prep_string(my_string):
    clean_string = my_string.strip()
    return clean_string

def count_words (my_string):
    count = my_string.count(' ') + 1
    return count

print(f'{count_words(prep_string(my_input))}')
