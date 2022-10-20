#!/usr/bin/python3
""" Contains the main app interface to guide the user
    on the use of the WebScrapping Tool
"""


import requests
from time import sleep
from var_pack import msg
from datetime import datetime
from bs4 import BeautifulSoup

# Wait time controller
sleep_time = 2

# Classes to process
classes = ['Offer']

# Constants
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
pages = ['https://mx.computrabajo.com/', 'https://co.computrabajo.com/']
countries = ['Mexico', 'Colombia']
currencies = ['MXP', 'COP']

# Temporal Variables
cur_pag = ""
cur_currency = ""
cur_country = ""
job_search = ""
num_offers = ""
my_url = ""
html_r = ""

def time_bar():
    now = datetime.now()
    ct = now.strftime("%H:%M:%S")
    print("\n" + msg.bar + ct + "\n")

def step0():
    """ Prints a Welcome Message to the screen """
    print("\n" + msg.bar + "\n\n" + msg.welcome)
    print(msg.intro1)
    print(msg.intro2)

def step1():
    """ Method used to select the URL WebScrapper to use """
    global cur_pag;
    time_bar()
    print(msg.quest1)

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
    """ Method used to select the country to set a currency """
    global cur_country, cur_currency;
    time_bar()
    print(msg.quest2)

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
    global job_search, my_url;
    time_bar()
    print(msg.quest3)

    answer = str(input("\n" + "R// "))

    if answer != 'null':
        job_search = answer
        print(msg.typed + job_search)
        my_url = cur_pag + "trabajo-de-" + job_search + '/?p=1'
    else:
        pass

def step4():
    """ Method used to get the number of offers to request """
    global num_offers;
    time_bar()
    print(msg.quest4)

    answer = int(input("\n" + "R// "))

    if answer != 'null':
        num_offers = answer
        print(msg.typed + str(num_offers))

    else:
        pass

def url_builder():
    """ Function used to build a URL """
    global cur_pag, job_search, num_offers, my_url, headers, html_r;
    time_bar()
    print(msg.search_for + str(num_offers) + " offers")
    print(msg.got_url + my_url)

    print("\n" + msg.quest5)
    answer = input("\n" + "R// ")

    if answer is int:
        return TypeError

    if answer == 'y' or 'yes':
        time_bar();
        print(msg.working)
        sleep(sleep_time)

        html_r = requests.get(my_url, headers=headers)
        print("\n" + msg.got_html + "\n" + msg.bar + "\n")
        sleep(sleep_time)
        html_process()

    else:
        print("Thanks, going back...")
        step1()

def html_process():
    """ """
    global html_r;
    now = datetime.now()
    ct = now.strftime("%H:%M:%S")
    buffer = {'get_date': ct,}

    soup = BeautifulSoup(html_r.text, 'html.parser')

    # Get Offer tittle
    try:
        offer_tittle = soup.find('h1', {'class': 'fwB fs24 mb5 box_detail w100_m'}).text
        buffer['Offer_tittle'] = offer_tittle
        print(buffer)
    except:
        buffer['Offer_tittle'] = 'N/A'
        print(buffer)
        print(msg.didnot_get)

    # Get Company Name
    try:
        comp_name = soup.find('a', {'class': 'dIB fs16 js-o-link'}).text
        buffer['Company'] = comp_name
        print(buffer)
    except:
        buffer['Company'] = 'N/A'
        print(buffer)
        print(msg.didnot_get)

    # Get Offer Location
    try:
        location = soup.find('p', {'class': 'fs16'}).text
        buffer['Location'] = location
        print(buffer)
    except:
        buffer['Location'] = 'N/A'
        print(buffer)
        print(msg.didnot_get)

    # Get Offer description
    try:
        description = soup.find('p', {'class': 'mbB'}).text
        buffer['Description'] = description
        print(buffer)
    except:
        buffer['Description'] = 'N/A'
        print(buffer)
        print(msg.didnot_get)

    # Get Offer Salary
    try:
        salary = soup.find('p', {'class': 'fwB fs21'}).text
        buffer['Salary'] = salary
    except:
        buffer['Salary'] = 'N/A'
        print(msg.didnot_get)


def get_url_list():
    """ """
    urls_ofertas = soup.find_all('a', 'js-o-link')

    # List of urls
    url_list = [my_url + urls.get('href') for urls in urls_ofertas]

    return(url_list)

    for page in range(1, num_offers+1):
        offers = get_urls_empleos(page)
        thread_list = list()

        for x in offers:
            t = threading.Thread(name='PROCESSING {}'.format(
                x), target=data_retrieval, args=(x,))
            thread_list.append(t)
            t.start()
            print(t.name + ' started!')
        for thread in thread_list:
            thread.join()
        print(f'PAGE {page} --- Data retrieval completed!')

step0();
step1();
step2();
step3();
step4();
url_builder();
html_process();

