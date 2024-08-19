def color_time(color: int):
    # return time for each color
    if color % 7 == 0:
        time = 13 * (color // 7)
    else:
        time = 13 * ((color // 7) + 1)
    return time

test_case = 0

while test_case < 10:
    orange, blue, green, yellow, pink, violet, brown, red = 0,0,0,0,0,0,0,0
    smarties_color = ''
    box_time = 0

    while smarties_color != 'end of box':
        smarties_color = input()
        if smarties_color == 'orange':
            orange = orange + 1
        elif smarties_color == 'blue':
            blue = blue + 1
        elif smarties_color == 'green':
            green = green + 1
        elif smarties_color == 'yellow':
            yellow = yellow + 1
        elif smarties_color == 'pink':
            pink = pink + 1
        elif smarties_color == 'violet':
            violet = violet + 1
        elif smarties_color == 'brown':
            brown = brown + 1
        elif smarties_color == 'red':
            red = red + 1

    box_time = color_time(orange) + color_time(blue) + color_time(green) \
        + color_time(yellow) + color_time(pink) + color_time(violet) \
        + color_time(brown) + (16 * red)
    test_case = test_case + 1
    print(f'{box_time}')
