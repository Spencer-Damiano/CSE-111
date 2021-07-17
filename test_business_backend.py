import pytest
import datetime
from random import randint
from random import choice
from business_backend import get_all_customer_dict, get_todays_date, new_customer_id, make_new_customer

def test_all_customers():
    all_dictionary = get_all_customer_dict()
    # for _ in range(1000):
    #     for key in all_dictionary.keys():
    #         assert new_customer_id() != key
    assert all_dictionary[12345] == {'first name': 'Spencer', 'last name': 'Damiano', 'serving size': 1.5, 'day joined': '2021-07-16'}
    assert all_dictionary[23456] == {'first name': 'Jack', 'last name': 'Damiano', 'serving size': 1.0, 'day joined': '2021-05-1'}

def test_get_todays_date():
    for _ in range(10):
        assert get_todays_date() == f'{datetime.date.today().year}-{datetime.date.today().month}-{datetime.date.today().day}'
    for _ in range(1000):
        year = randint(1000, 9999)
        month = randint(1, 12)
        month = str(month)
        if len(month) == 1:
            month = '0{month}'
        day = randint(1 , 31)
        assert get_todays_date(set_date=True, year=year, month=month, day=day) == f'{year}-{month}-{day}'

def test_new_customer_id():
    """
    this does have it's limits. because of the range we will run out of id's after a point
    """
    all_dictionary = get_all_customer_dict()
    for _ in range(1000):
        for key in all_dictionary.keys():
            assert new_customer_id() != key

def test_make_new_customer():
    list_first_names = ['Joe', 'Donald', 'Brack', 'George W.', 'Bill', 'George H. W.', 'Ronald', 'Jimmy']
    list_last_names = ['Biden', 'Trump', 'Obama', 'Bush', 'Clinton', 'Bush', 'Reagan', 'Carter']
    for _ in range(10):
        id_num = new_customer_id()
        first_name = choice(list_first_names)
        last_name = choice(list_last_names)
        serving_size = randint(1, 5) 
        for _ in range(1):
            year = randint(1000, 9999)
            month = randint(1, 12)
            month = str(month)
            if len(month) == 1:
                month = f'0{month}'
            day = randint(1, 31)
            day_joined = f'{year}-{month}-{day}'
        make_new_customer(pre_input=True, id_num=id_num, first_name=first_name,last_name=last_name,serving_size=serving_size,day_joined=day_joined)
        all_customers_dict = get_all_customer_dict()
        print(all_customers_dict)
        assert all_customers_dict[id_num] == {'first name': first_name, 'last name': last_name, 'serving size': serving_size, 'day joined': day_joined}


pytest.main(["-v", "--tb=line", "-rN", "test_business_backend.py"])