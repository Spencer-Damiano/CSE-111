import datetime

"""
This program has two parts. a main which runs the byui income and then 
a plasma main which was created because the plasma money has more varibles and 
is harder to predict and control.
"""


def main():
    pay = 9.8
    print('hello and welcome to the budget \n')

def find_byui_income(hours, pay):
  money = hours * pay

  taxed = input('taxed y/n')
  post_tax = .9235
  if taxed == 'y':
    money = money * post_tax

  return money

def plasma_main():
    print('welcome to the plasma main \n')

def find_total_plasma_money(times):
  count = 0
  money = 0
  for _ in range(times):
    money += 25 + 5 * count
    count += 1
  money += int(input('bonus? $'))
  return money

def print_calendar():
    date = datetime.datetime.now()
    print(date)

print_calendar()