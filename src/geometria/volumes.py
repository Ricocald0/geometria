import math
#volume_box
def volume_box(length, width, height):
    return length * width * height
#volume_cone
def volume_cone(radius, height):
    return (math.pi * radius**2 * height) / 3
#volume_sphere
def volume_sphere(radius):
    return (4 * math.pi * radius**3) / 3
   