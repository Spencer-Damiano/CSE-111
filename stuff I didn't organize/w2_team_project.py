from datetime import datetime
current = datetime.now()
weekday = current.isoweekday()

subtotal = 0
run = True
while run:
    items = int(input('how many items do you have? ')) 
    price = int(input('how much do they cost? '))
    sub_subtotal = items * price
    subtotal += sub_subtotal
    continue_run = input('do you want to keep adding items? y/n')
    if continue_run == 'n':
        run = False


    
def get_discount(subtotal, weekday):
    if weekday == 2 or 3:
        if subtotal >= 50:
            subtotal = subtotal * .9
    
    tax = subtotal * .06
    total = subtotal + tax
    print(f"Discount Price: {subtotal:.2f}")
    print(f"Sales Tax: ${tax:.2f}")
    print(f"Your toal is: ${total:.2f}")

get_discount(subtotal, weekday)

