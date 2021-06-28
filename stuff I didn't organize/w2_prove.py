import math

def find_tire_volume(current_date):
    width = int(input('what is the width (in mm) of the tire? '))
    aspect_ratio = int(input('what is the aspect ratio of the tire? '))
    diameter = int(input('wha tis the diameter (in inches) of the wheel? '))

    v = round((math.pi * (width * width) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000, 1)
    tire_volume = str(v)
    input_to_volumes = str(current_date) + ', ' + str(width) + ', ' + str(aspect_ratio) + ', ' + str(diameter) + ', ' + str(v)

    with open('volumes.txt', mode='a') as text_file:
        print(f'{input_to_volumes}', file=text_file)

    return tire_volume

run = True
first_time = True

while run:
    from datetime import datetime
    current_date = (datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-7])
    if first_time:
        print('welcome to find your tire pressure, please enter to following information below:')
        print()
        print(find_tire_volume(current_date))
        first_time = False
    elif first_time == False:
        next_tire = input('would you like to add another tire? y/n ')
        if next_tire == 'y':
            print(find_tire_volume(current_date))
        elif next_tire == 'n':
            run = False
            print('thanks for using my program :)')
        else:
            print('something has gone terribly wrong - another tire')
    else:
        print('something has gone terribly wrong - first time')
        run = False

