sentence = input()
i = 0
result = ''

while i < len(sentence):
    result = result + sentence[i]
    if sentence[i] in 'aeiuo':
        i = i + 3
    else:
        i = i + 1
print(result)
