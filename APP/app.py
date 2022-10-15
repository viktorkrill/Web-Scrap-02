#!/usr/bin/python3
""" Contains the main app interface to guide the user
    on the use of the WebScrapping Tool
"""
import requests
from time import sleep
from var_pack import msg

# wait time controller
sleep_time = 2

# Classes to process
classes = ['Offer']

# Constants1
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
pages = ['https://mx.computrabajo.com/', 'https://co.computrabajo.com/']
currencies = ['MXP', 'COP']
countries = ['Mexico', 'Colombia']

# Temporal Variables
cur_pag = ""
cur_currency = ""
cur_country = ""
job_search = ""
num_offers = ""
my_url = ""


def welcome():
    """ Prints a Weolcome Message to the screen """
    print("\n" + msg.welcome)
    print("\n" + msg.intro)

def step1():
    """ Method used to select a web page to look into """
    global cur_pag;
    print("\n" + msg.quest1)

    for i, page in enumerate(pages):
        print(i, page)

    answer = int(input("\n" + "R// "))

    if answer == 0:
        cur_pag = pages[0]
        print(msg.selection + cur_pag)

    if answer == 1:
        cur_pag = pages[1]
        print(msg.selection + cur_pag)

    else:
        pass

def step2():
    """ Method used to select the country where to look for offers """
    global cur_country, cur_currency;
    print("\n" + msg.quest2)

    for i, country in enumerate(countries):
        print(i, country)

    answer = int(input("\n" + "R// "))

    if answer == 0:
        cur_country = countries[0]
        cur_currency = currencies[0]
        print(msg.selection + cur_country)
        print(msg.currency_format + cur_currency)

    if answer == 1:
        cur_country = countries[1]
        cur_currency = currencies[1]
        print(msg.selection + cur_country)
        print(msg.currency_format + cur_currency)

    else:
        pass

def step3():
    """ Method used to get the Position or Role to search """
    global job_search;
    print("\n" + msg.quest3)

    answer = str(input("\n" + "R// "))

    if answer != 'null':
        job_search = answer
        print(msg.typed + job_search)

    else:
        pass

def step4():
    """ Method used to get the number of offers to request """
    global num_offers;
    print("\n" + msg.quest4)

    answer = int(input("\n" + "R// "))

    if answer != 'null':
        num_offers = answer
        print(msg.typed + str(num_offers))

    else:
        pass

def urL_builder():
    """ Method used to get the number of offers to request """
    global cur_pag, job_search, my_url, headers;
    print("\n" + msg.got_url)
    my_url = cur_pag + "trabajo-de-" + job_search
    print(my_url)

    print("\n" + msg.quest5)
    answer = input("\n" + "R// ")

    if answer == 'y' or 'yes':
        print("\n" + msg.working)
        sleep(sleep_time)
        r = requests.get(my_url, headers=headers)
        print("\n" + msg.got_html)
        sleep(sleep_time)
        print(r.content)

    else:
        print("Thanks, going back...")
        step1()

# def make_request():
welcome();

step1();
print(cur_pag)

step2();
print(cur_country + " = " + cur_currency)

step3();
print("Your are looking for: " + job_search)

step4();
print("You are expecting for: " + str(num_offers) + " results")

urL_builder();
print(my_url)
