import math

def find_tire_volume():
    width = int(input('what is the width (in mm) of the tire? '))
    aspect_ratio = int(input('what is the aspect ratio of the tire? '))
    diameter = int(input('wha tis the diameter (in inches) of the wheel? '))

    v = round((math.pi * (width * width) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000, 1)
    tire_volume = v
    return tire_volume

run = True
while run == True:
    if run == True:
        print(find_tire_volume())
        continue_run = input('do you want to inout another tire? y/n ').lower()
        if continue_run == 'n':
            run = False


