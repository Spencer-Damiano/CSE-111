import math

def needed_boxes():
    items = int(input('how many items do you have? '))
    per_box = int(input('how many items per box? '))
    boxes_needed = math.ceil(items / per_box)
    return boxes_needed


print(needed_boxes())