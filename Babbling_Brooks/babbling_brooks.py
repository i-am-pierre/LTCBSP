n = int(input())
stream_map = []

def split_stream(stream_list: list, split_point: int, left_split:int ):
    # Function to modify my list with a split
    pre = stream_list[:split_point - 1]
    post = stream_list[split_point:]
    volume = stream_list[split_point - 1]
    l = round(volume * ( left_split / 100 ))
    r = volume - l
    new_stream = pre[:] + [l] + [r] + post[:]
    return new_stream

def join_stream(stream_list: list, join_point: int):
    # Function to modify my list with a join
    volume = sum(stream_list[join_point - 1 : join_point + 1])
    pre = stream_list[:join_point - 1]
    post = stream_list[join_point + 1:]
    new_stream = pre[:] + [volume] + post[:]
    return new_stream

# Build initial number of streams at some high altitude in list
for i in range(n):
    stream = int(input())
    stream_map.append(stream)

action = int(input())
while action != 77:
    if action == 99:
        split = int(input())
        left = int(input())
        stream_map = split_stream(stream_map, split, left)
    elif action == 88:
         point = int(input())
         stream_map = join_stream(stream_map, point)
    action = int(input())

# Format list of int into list of strings
stream_map_string = map(str, stream_map)

# Join string togteher
answer = ' '.join(stream_map_string)

print(answer)
