my_password = input()

def test_length(word:str):
    # test if lenght is between 8 and 12
    length = len(word)
    if length >= 8 and length <= 12:
        return True
    else:
        return False

def test_alphanumerical(word:str):
    #test if string is alphanumerical only
    return word.isalnum()

def test_at_least_three_low(word:str):
    # test if at least 3 lower cases letters
    count = 0
    for char in word:
        if char.islower():
            count = count + 1
            if count > 2:
                return True
    return False

def test_at_least_two_upp(word:str):
    # test if at least 2 upper cases letters
    count = 0
    for char in word:
        if char.isupper():
            count = count + 1
            if count > 1:
                return True
    return False

def test_at_least_one_digit(word:str):
    # test if at least 1 upper cases letters
    for char in word:
        if char.isdigit():
            return True
    return False

def verify_password(word:str):
    # Combine the prompt to verify
    if test_length(word) and test_alphanumerical(word) and\
        test_at_least_three_low(word) and test_at_least_two_upp(word) and\
            test_at_least_one_digit(word):
        return 'Valid'
    else:
        return 'Invalid'
    
results = verify_password(my_password)
# print(f'test length: {test_length(my_password)}')
# print(f'test Alphnumerical: {test_alphanumerical(my_password)}')
# print(f'test at least 3 lower chars: {test_at_least_three_low(my_password)}')
# print(f'test at lest 2 upper chars: {test_at_least_two_upp(my_password)}')
# print(f'test at least 1 digit: {test_at_least_one_digit(my_password)}')

print(results)
