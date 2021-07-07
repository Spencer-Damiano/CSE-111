import calendar
import datetime 

# I will use gobal varibles so if tax rates, hourly wage, or anthing else comes up
hourly_pay = 9.8
tax_rate = .9235

def main():
  byui_money = round(byui_main(), 2)
  plasma_money = round(plasma_main(), 2)
  income = round(byui_money + plasma_money, 2)

  run_taxes = input('are you expecting to get taxed? y/n ')

  if run_taxes == 'y':
    taxes = round(get_tax(byui_money), 2)
  else:
    taxes = 0

  tithing = round(pay_the_lord(income), 2)

  net_income = round(income - (taxes + tithing), 2)
  
  print()
  print('Income - ')
  print(f'Byu-Idaho money: {byui_money}')
  print(f'Plasma Money: {plasma_money}')
  print()
  print(f'taxes - {taxes} tithing - {tithing}')
  print(f'net income - {net_income}')




def byui_main():
  """
  This uses an input of how many hours I am projecting to work. this estimation will be based on a monthly reponse
  return ttl_money
  """
  ttl_money = 0
  run_times = int(input('how many pay periods are you planning out for? '))

  for i in range(run_times):
    hours = float(input('how many hours are you planning on working this pay period? '))
    pay_check = hours * hourly_pay
    print(f'pay period {i} will be {pay_check}')

    ttl_money += pay_check
  return ttl_money


def plasma_main():
  """
  This will use the calender to show what date's plasma is donated and the amount of money that will come with that. a count in a list will keep track of times donated. By having a record of what day you donate you can project when the best times to donate are. This hopefully should be a good way to navigate the bonus.
  return ttl_money
  """
  ttl_plasma_money = 0

  year = datetime.date.today().year
  month = datetime.date.today().month

  print_calendar(year, month)

  multi_month = int(input('how many months are you planning for? '))

  for _ in range(multi_month):

    donations = int(input('how many times are you going donate this month. '))

    ttl_plasma_money += get_plasma_base(donations)

    bonus = input('do you have any bonuses? y/n ')

    if bonus == 'y':
      ttl_plasma_money += get_plasma_bonus()
    elif bonus == 'n':
      print('that\'s strange but ok')
    else:
      print('plasma_fail failed at bonus')

  return ttl_plasma_money



def print_calendar(year, month):
  """
  This function prints the calendar for user to pick the days they want to donate plasma
  it just prints the calendar. Might use this information to find the best days to go and donate to get the best money for the month.
  """
  c = calendar.TextCalendar(calendar.SUNDAY)
  str = c.formatmonth(year, month)

  print()
  print(str)

def get_plasma_base(donations):
  donation_count = 0
  ttl_money = 0

  for i in range(donations):
    donation_money = 25 + 5 * donation_count
    if donation_money <= 50:
      ttl_money += donation_money
    elif donation_money > 50:
      ttl_money += 50 
    donation_count += 1
    if donation_count > donations:
      break
  
  return ttl_money

def get_plasma_bonus():

  ttl_money = 0

  def twenty_five_second():
    """
    This section gives you $25 for every second time in a week. It asks people how many times you donate twice in a week for simplicty reasons. 
    * posible update to take donations / 2 and round down
    return bonus_money
    """
    second_times = int(input('how many second apointments are you planning on?'))

    bonus_money = second_times * 25

    return bonus_money
  
  def hundo_on_six():
    hundo = input('did you donate six times for $100 y/n')

    if hundo == 'y':
      bonus_money = 100

    return bonus_money


  bonus_run = int(input('how many bonuses are there this month? '))

  for _ in range(bonus_run):
    bonus = input('what bonus are there this month? 25on2 or 100on6 ')

    if bonus == '25on2':
      ttl_money += twenty_five_second()
    elif bonus == '100on6':
      ttl_money += hundo_on_six()

  return ttl_money

def get_tax(byui_money):
  taxes = byui_money - (byui_money * tax_rate)

  return taxes


def pay_the_lord(income):
  tithing = income * .1

  return tithing

main()