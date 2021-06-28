
from os import replace


def main():
    # print the list.
    provinces_list = read_list('provinces.txt')

    for _ in provinces_list:
        print(_)

    provinces_list = delete_from_list(provinces_list)

    print(provinces_list)

    provinces_list = replace_ab(provinces_list)
    print(provinces_list)

    alberta_count = alberta_counter(provinces_list)

    print(f'the alberta couner is {alberta_count}')



def read_list(file):
    provinces_list = []

    with open(file, 'rt') as text_file:

        for line in text_file:
            strip_line = line.strip()

            provinces_list.append(strip_line)

    return provinces_list

def delete_from_list(provinces_list):

    provinces_counter = 0

    for _ in provinces_list:
        if provinces_counter == 0:
            provinces_list_deleted = provinces_list[1:-1]
    
    return provinces_list_deleted

def replace_ab(provinces_list):
    
    new_list = []

    for AB in provinces_list:
        if AB == 'AB':
            AB = 'Alberta'
            new_list.append(AB)
        elif AB != 'AB':
            new_list.append(AB)
    
    return new_list

def alberta_counter(provinces_list):

    counter = 0

    for _ in provinces_list:
        if _ == 'Alberta':
            counter += 1

    return counter




main()