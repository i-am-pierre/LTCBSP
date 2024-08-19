from icecream import ic

# Get inputs line one for number of platform
NB_OF_PLATFORM = int(input())

raw_list_of_platforms = []

for lines in range(NB_OF_PLATFORM):
  platform = list(map(int, input().split()))
  raw_list_of_platforms.append(platform)

# sort my list of platforms from highest to lowest
sorted_list_of_platforms = sorted(raw_list_of_platforms, key=lambda x: x[0], reverse=True)

def current_height_list(height: int, list_of_platforms:list) -> list:
  """
  Function that takes a Height and returns a sub-list of platforms for that 
  height and lower down
  """
  for platform in list_of_platforms[:]:
    if height >= platform[0]:
      return list_of_platforms
    else:
      return current_height_list(height, list_of_platforms[1:])


def is_touching_ground(X:int, Y:int, list_of_platforms:list) -> bool:
  """
  Function that checks if a leg of a platform is touching the ground
  """
  l = current_height_list(Y, list_of_platforms)
  if Y == 1 or len(l) == 0 or len(l) == 1:
    return True
  else:
    return (X <= l[1][1] or X >= l[1][2]) and (is_touching_ground(X, Y, l[1:]))
  
  # TODO: create a function that returns the value of the height of the platform it intersect.





# ic(is_touching_ground(5, 1, sorted_list_of_platforms))
# ic(is_touching_ground(10, 1, sorted_list_of_platforms))

# ic(is_touching_ground(3, 5, sorted_list_of_platforms))
# ic(is_touching_ground(7, 5, sorted_list_of_platforms))



# ic(is_touching_ground(1, 3, sorted_list_of_platforms))
# ic(is_touching_ground(5, 3, sorted_list_of_platforms))
