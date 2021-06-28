import csv

search = []
count = 0
viehicle_delete = 0

with open('fuel_errors.csv') as fuel_errors:
    read_fuel = csv.reader(fuel_errors)
    for row in read_fuel:
        viehicle = row[0]
        if viehicle_delete == 0:
            viehicle = viehicle[13:]
            viehicle_delete += 1
        elif viehicle_delete == 1:
            viehicle = viehicle[10:]
        else:
            print('that didn\'t work')

        
        #print(viehicle)

        odometer = row[1]
        odometer = odometer[10:]
            #print(odometer)

        current_odometer = row[3]
        current_odometer = current_odometer[53:]
        current_odometer = current_odometer[:-1]  
        #current_odometer = current_odometer - 1
            # print(current_odometer)

        new_line = viehicle + ', ' + odometer + ', ' + current_odometer
        search.append(new_line) 

        with open('fuel_errors_post.csv', 'w', newline='') as new_list:
            for line in search:
                new_list.write(line + '\n')


print('I think its done')