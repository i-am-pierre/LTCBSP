def my_status(w:int, c:int):
    if w == 3 and c > 94:
        return "absolutely"
    elif w == 1 and c < 51:
        return "fairly"
    else:
        return "very"
    
my_w = int(input())
my_c = int(input())

CCstatus = my_status(my_w, my_c)

print(f'C.C. is {CCstatus} satisfied with her pizza.')
