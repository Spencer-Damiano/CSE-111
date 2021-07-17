import datetime 
import pandas as pd
from random import randint
from random import choice
from csv import writer

def get_all_customer_dict(test=False):
  """
  This will return the customer csv file
  """
  if test == False:
    usable_dict = {}
    df = pd.read_csv('rocko_customer.csv')
    customers = df.to_dict()
    all_ids = customers['customer id']
    all_first_names = customers['first name']
    all_last_names = customers['last name']
    all_serving_sizes = customers['serving size']
    all_days_joined = customers['day joined']
    counter = 0
    for customer in range(len(all_ids)):
        id = all_ids[counter]
        first_name = all_first_names[counter]
        last_name = all_last_names[counter]
        serving_size = all_serving_sizes[counter]
        day_joined = all_days_joined[counter]
        usable_dict[id] = {
            'first name': first_name,
            'last name': last_name,
            'serving size': serving_size,
            'day joined': day_joined
        }
        counter += 1
    return usable_dict
  elif test == True:
    usable_dict = {}
    df = pd.read_csv('test_rocko_customer.csv')
    customers = df.to_dict()
    all_ids = customers['customer id']
    all_first_names = customers['first name']
    all_last_names = customers['last name']
    all_serving_sizes = customers['serving size']
    all_days_joined = customers['day joined']
    counter = 0
    for customer in range(len(all_ids)):
        id = all_ids[counter]
        first_name = all_first_names[counter]
        last_name = all_last_names[counter]
        serving_size = all_serving_sizes[counter]
        day_joined = all_days_joined[counter]
        usable_dict[id] = {
            'first name': first_name,
            'last name': last_name,
            'serving size': serving_size,
            'day joined': day_joined
        }
        counter += 1
    return usable_dict


 
def open_recipe_csv():
  """
  this will open the recipe csv file
  """
  recipies = pd.read_csv('recipies.csv')
  return recipies


def get_todays_date(set_date=False, year=None, month=None, day=None):
  if set_date == False:
    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day
    return(f'{year}-{month}-{day}')
  elif set_date == True:
    return(f'{year}-{month}-{day}')
    

def new_customer_id():
    double_check = []
    customer_dict = get_all_customer_dict()
    for key in customer_dict.keys():
        double_check.append(key)
    while True:
        range_start = 10000
        range_end = 99999
        id = randint(range_start, range_end)
        if id not in double_check:
            return id


def make_new_customer(pre_input=False, id_num=None, first_name=None, last_name=None, serving_size=None, day_joined=None):
    new_customer = []
    if pre_input == True:
      new_customer.append(id_num)
      new_customer.append(first_name)
      new_customer.append(last_name)
      new_customer.append(serving_size)
      new_customer.append(day_joined)
      # print(f'why this no work : {new_customer}')
      add_newbie_to_csv(new_customer, test=True)
    else:
      while True:
        try:
          id_num = new_customer_id()
          new_customer.append(id_num)
          first_name = input('what is your first name? ').capitalize()
          new_customer.append(first_name)
          last_name = input('what is your last name? ').capitalize()
          new_customer.append(last_name)
          print('With the serving size please enter number ex: 1 or 1.5')
          serving_size = float(input('how many serving sizes do you want? '))
          new_customer.append(serving_size)

          while True:
            try:
              custom_date = input('would you like to enter a day joined that is not today? y/n ')
              assert custom_date == 'y' or custom_date == 'n'
              if custom_date == 'n':
                day_joined = get_todays_date()
                new_customer.append(day_joined)
                break
              elif custom_date == 'y':
                year = input('what year did you join? ')
                assert len(year) == 4
                month = int(input('what month did you join? '))
                assert month <= 12
                month = str(month)
                if len(month) == 1:
                  month = f'0{month}'
                  assert len(month) == 2
                day = input('what day did you join? ')
                forbiden_days = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
                assert len(day) == 1
                assert day <= 31
                assert len(day) == 2
                assert day not in forbiden_days
                day_joined = f'{year}-{month}-{day}'
                new_customer.append(day_joined)
                break
            except AssertionError:
              print('you have enter something in incorectly')
              print('please enter either y or n for a custom date')
              print('please enter the date info as number ex:')
              print('year as 2021 or 1998')
              print('month as 11 or just a single didgit without a 0 in front ex: 1')
              print('the day as 21 or just a single didgit without a 0 in front ex: 5')
              print()
        except ValueError:
          print('you have entered the wrong value type into a response')
          print('you either put a number as your name or typed out the number instead of putting 1 or 1.5')
          new_customer = []
        except AssertionError:
          print('Please renter your information and for custom date put either a y or a n')
          new_customer = []
        add_newbie_to_csv(new_customer)
        break


def add_newbie_to_csv(new_customer_info, test=False):
  if test == False:
    with open('rocko_customer.csv', 'a') as newbie:
      writer_csv = writer(newbie)
      writer_csv.writerow(new_customer_info)

      newbie.close()
    print('customer added')
  elif test:
    with open('test_rocko_customer.csv', 'a') as newbie:
      writer_csv = writer(newbie)
      writer_csv.writerow(new_customer_info)

      newbie.close()
    print('test customer added')