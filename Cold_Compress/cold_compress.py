nb_lines = int(input())

string_index = 0

while string_index < nb_lines:
    string = input()
    encoded_string = ''
    counter = 1
    current_char = string[0]
    for char in string[1:]:
        next_char = char
        if current_char == next_char:
            counter = counter + 1
        else:
            encoded_string = encoded_string + ' ' + str(counter) + ' ' + current_char
            current_char = next_char
            counter = 1
    encoded_string = encoded_string + ' ' + str(counter) + ' ' + current_char
    print(encoded_string)
    string_index = string_index + 1
