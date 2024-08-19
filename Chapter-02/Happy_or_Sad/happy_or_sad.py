def my_mood (my_string):
    # Compare happy and sad count to return appropriate string
    happy_count = my_string.count(":-)")
    sad_count = my_string.count(":-(")
    if (happy_count == 0 and sad_count == 0):
        return "none"
    elif (happy_count > sad_count):
        return "happy"
    elif (happy_count == sad_count):
        return "unsure"
    else:
        return "sad"

mood = input()
answer = my_mood(mood)

print(f"{answer}")
