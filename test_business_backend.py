import pytest
import datetime
from random import randint
from business_backend import get_all_customer_dict, get_todays_date, new_customer_id

def test_all_customers():
    all_dictionary = get_all_customer_dict()
    for _ in range(1000):
        for key in all_dictionary.keys():
            assert new_customer_id() != key
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

pytest.main(["-v", "--tb=line", "-rN", "test_business_backend.py"])