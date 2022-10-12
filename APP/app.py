#!/usr/bin/python3
""" Contains the main app interface to guide the user
    on the use of the WebScrapping Tool
"""

import time
from var_pack import msg

# Welcome Messages
print("\n" + msg.welcome)
print("\n" + msg.intro)

sleep_time = 1

# Classes to process
classes = ['Offer', 'req_date', 'tittle', 'company', 'location', 'salary', 'currency']

# Variables to use
pages = ['https://mx.computrabajo.com/', 'https://co.computrabajo.com/']
currencies = ['MXP', 'COP']
countries = ['Mexico', 'Colombia']

# Temporal Variables
cur_page = ""
cur_currency = ""
cur_country = ""
job_search = ""
num_offers = ""
my_url = ""


def step1():
    """ Method used to select a web page to look into """
    print("\n" + msg.quest1)
    for i, page in enumerate(pages):
        print(i, page)
    try:
        answer = int(input("\n" + "R// "))
    except ValueError:
        print(msg.bad_selection)
    if answer == 0:
        cur_page = pages[0]
        print(msg.selection + cur_page)
        time.sleep(sleep_time)
    if answer == 1:
        cur_page = pages[1]
        print(msg.selection + cur_page)
        time.sleep(sleep_time)
    else:
        pass

def step2():
    """ Method used to select the country where to look for offers """
    print("\n" + msg.quest2)
    for i, country in enumerate(countries):
        print(i, country)
    try:
        answer = int(input("\n" + "R// "))
    except ValueError:
        print(msg.bad_selection)
    if answer == 0:
        cur_country = countries[0]
        cur_currency = currencies[0]
        print(msg.selection + cur_country)
        print(msg.currency_format + cur_currency)
        time.sleep(sleep_time)
    if answer == 1:
        cur_country = countries[1]
        cur_currency = currencies[1]
        print(msg.selection + cur_country)
        print(msg.currency_format + cur_currency)
        time.sleep(sleep_time)
    else:
        pass

def step3():
    """ Method used to get the Position or Role to search """
    print("\n" + msg.quest3)
    answer = str(input("\n" + "R// "))

    if answer != 'null':
        job_search = answer
        print(msg.typed + job_search)
        time.sleep(sleep_time)
    else:
        pass

def step4():
    """ Method used to get the number of offers to request """
    print("\n" + msg.quest4)
    try:
        answer = int(input("\n" + "R// "))
    except ValueError:
        print(msg.bad_selection)
    if answer != 'null':
        num_offers = answer
        print(msg.typed + str(num_offers))
        time.sleep(sleep_time)
    else:
        pass

# def make_request():

step1();
step2();
step3();
step4();
