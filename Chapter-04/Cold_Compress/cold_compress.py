nb_lines = int(input())

string_index = 0

while string_index < nb_lines:
    string = input()
    encoded_str = ''
    counter = 1
    current_char = string[0]
    for char in string[1:]:
        next_char = char
        if current_char == next_char:
            counter = counter + 1
        else:
            encoded_str = encoded_str + ' ' + str(counter) + ' ' + current_char
            current_char = next_char
            counter = 1
    encoded_str = encoded_str + ' ' + str(counter) + ' ' + current_char
    print(encoded_str)
    string_index = string_index + 1
