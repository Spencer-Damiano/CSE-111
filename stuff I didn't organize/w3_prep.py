
def main():
    start_od = int(input('what is the starting Odometer? '))
    end_od = int(input('what is the end odometer? '))
    gallons = float(input('how many gallons of gas did it take to travel that far? '))

    mpg = round(get_miles_per_gallon(start_od, end_od, gallons), 1)

    lpk = round(lp100k_from_mpg(mpg), 2)

    print(f'you car is getting {mpg} miles per gallon and getting {lpk} liters per killometer')



def get_miles_per_gallon(start_od, end_od, gallons):
    mpg = (end_od - start_od) / gallons

    return mpg


def lp100k_from_mpg(mpg):
    lpk = 235.215 / mpg

    return lpk

main()