PI = 3.141592653589793

radius = int(input())
height = int(input())

def cone_volume (r, h):
    volume = (PI * r**2 * h) / 3
    return volume

print(f'{cone_volume(radius, height)}')
