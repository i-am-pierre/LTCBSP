american_word = input()

while american_word != 'quit!':
    canadian_word = american_word[:]
    if len(american_word) > 4 and american_word[-2:] == 'or':
        if american_word[-3] != 'a' and american_word[-3] != 'e' and \
            american_word[-3] != 'i' and american_word[-3] != 'o' and \
                american_word[-3] != 'u' and american_word[-3] != 'y':
            canadian_word = american_word[0:-2] + 'our'
    print(f'{canadian_word}')
    american_word = input()
