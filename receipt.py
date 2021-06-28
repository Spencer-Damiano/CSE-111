import csv
from datetime import datetime

def main():
    product_dict = make_product_dict()

    order = get_order(product_dict)

    print_receipt(order)



def make_product_dict():
    with open('products.csv') as csv_products:
        read_products = csv.reader(csv_products)
        
        products = {}
        test_count = 0

        for row in read_products:
            product_info = []
            product_num = row[0]
            product_name = row[1]
            product_price = row[2]
            product_info.append(product_name)
            product_info.append(product_price)
            if test_count == 0:
                test_count += 1
            else:
                products[product_num] = product_info
        
        return products

def get_order(product_dict):
    count = 0
    reciept = []
    file_name = input('would you like a recipt? y/n ')

    while True:
        
        assert file_name == 'y' or file_name == 'n'

        try:
            if file_name == 'n':
                reciept = get_custom_order(product_dict)
                break
            elif file_name == 'y':
                with open('request.csv') as order_request:
                    read_order = csv.reader(order_request)

                    for row in read_order:
                        if count == 0:
                            count += 1
                        elif count > 0:
                            product_code = row[0]
                            amount = row[1]

                            product_info = product_dict[product_code]

                            receipt_info = get_amount_price(product_info, amount)
                            reciept.append(receipt_info)
                    break
        except AssertionError as failed_receipt_request:
            print('please enter either y or n')
        break
    return reciept



def get_custom_order(products):
    run = True
    fail_safe = 0

    recipet = []

    while True:
        try:
            easter_egg = input('would you like an easter egg? y/n ')
            assert easter_egg == 'y' or easter_egg == 'n'

            if easter_egg == 'n':
                print('you\'re lame')
                run = False
                break
            elif easter_egg == 'y':
                print('welcome to make your own shopping cart')
            

            break
        except AssertionError as easter_egg_fail:
            print('you have to enter y or n')

    while run:
        print_product_list(products)

        
        print('To stop adding something to your cart please type \'quit\'')
        user_choice = input('what is the item code you would like to add? ')
        fail_safe += 1
        if fail_safe > 20:
            bail = input('you might be in an infinate loop, do you want out? y/n ')
            if bail == 'y':
                break
        try:
            if user_choice == 'quit':
                break
            product = products[user_choice]
            product_amount = int(input('how many would you like? '))
            assert product_amount > 0
            recipet.append(get_amount_price(product, product_amount))


        except KeyError as bad_user_coice:
            print('you must have entered to code wrong, please try again...')
        except ValueError as not_an_int:
            print('please enter your product as a whole number ex: \'3\'')
        except AssertionError as neg_num:
            print('you need to have a number higher than one')

    return recipet

        
    

def print_product_list(products):
    for key, value in products.items():
        value_list = []
        print(f'{value[0]}, {value[1]} -- Code: {key}')

def get_amount_price(product_info, amount):
    recipet_info = []
    
    product_name = product_info[0]
    recipet_info.append(product_name)

    num_products = int(amount)
    recipet_info.append(num_products)

    product_price = float(product_info[1])
    recipet_info.append(product_price)


    amount_price = num_products * product_price
    amount_price = round(amount_price, 2)
    recipet_info.append(amount_price)

    return recipet_info

def print_receipt(recipet):
    sub_ttl = 0
    item_count = 0
    current_date_and_time = datetime.now()

    print('-' * 31)
    print('welcome to Damiano and Sons')
    print()
    for info in recipet:
        product_name = info[0]
        product_amount = info[1]
        item_count += product_amount
        product_price = info[2]
        sub_ttl += info[3]

        print(f'{product_name}: {product_amount} @ {product_price}')
    print()
    print(f'Number of Items {item_count}')
    sub_ttl = round(sub_ttl, 2)
    print(f'Subtotal: {sub_ttl}')
    sales_tax = round(sub_ttl * .06, 2)
    print(f'Sales Tax: {sales_tax}')
    total = round(sub_ttl + sales_tax, 2)
    print(f'Total: {total}')
    print()
    print('Thank you for shopping with us!')
    print(f"{current_date_and_time:%A %I:%M %p}")
    print('-' * 31)

main()
