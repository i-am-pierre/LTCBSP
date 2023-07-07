test_word = input()

def honi_count(word:str):
    count = 0
    has_h = False
    has_o = False
    has_n = False
    has_i = False
    for char in word:
        if char == 'H':
            has_h = True
        elif has_h and char == 'O':
            has_o = True
        elif has_h and has_o and char == 'N':
            has_n = True
        elif has_h and has_o and has_n and char == 'I':
            count = count + 1
            has_h = False
            has_o = False
            has_n = False
            has_i = False
    return count

result = honi_count(test_word)
print(f'{result}')
