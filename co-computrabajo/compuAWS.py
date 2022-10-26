import threading
import json
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
import os
import requests
import re
from db.models import storage
from db.models.job_offer import JobOffer


# Parse html
def get_urls_empleos(num):

    url = 'https://co.computrabajo.com/trabajo-de-aws-developer/?p={}'.format(
        num)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Boxes
    urls_ofertas = soup.find_all('a', 'js-o-link')

    # List of urls
    lista_url_empleos = ['https://www.computrabajo.com.co' +
                         urls.get('href') for urls in urls_ofertas]

    return(lista_url_empleos)


# info date
def data_retrieval(url):

    fecha_busqueda = datetime.today().strftime('%Y-%m-%d-%H-%M')

    registro = {
        'url_empleo': url,
        'fecha_recuperacion': fecha_busqueda,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    # Ofert title
    try:
        titulo_oferta = soup.find(
            'h1', {'class': 'fwB fs24 mb5 box_detail w100_m'}).text
        registro['Titulo_oferta'] = titulo_oferta
    except:
        registro['Titulo_oferta'] = 'N/A'
        print('no se recupero titulo de la oferta')

    # Company name
    try:
        emp = soup.find('a', {'class': 'dIB fs16 js-o-link'}).text
        registro['Empresa'] = emp

    except:
        registro['Empresa'] = 'N/A'
        print('no re recupero empresa')

    # City
    try:
        ubicacion = soup.find('p', {'class': 'fs16'}).text
        registro['Ubicacion'] = ubicacion
    except:
        registro['Ubicacion'] = 'N/A'
        print('no se recupero ubicacion')

    # Description
    try:
        descripcion = soup.find('p', {'class': 'mbB'}).text
        registro['Descripcion'] = descripcion
    except:
        registro['Descripcion'] = 'N/A'
        print('no se recupero la descripcion')

    # Requirements
    try:
        requerimientos = ''
        reque = soup.find('ul', {'class': 'disc mbB'}).find_all('li')
        for i in reque:
            requerimientos = requerimientos + i.text + ';'
        registro['Requerimientos'] = requerimientos

    except:
        registro['Requerimientos'] = 'N/A'
        print('no se recupero requerimientos')

    # Salary
    try:
        salario = soup.find('p', {'class': 'fwB fs21'}).text
        registro['Salario'] = salario
    except:
        registro['Salario'] = 'N/A'
        print('no se recupero salario')

    # Create files json
    id_job_by_url = re.search("[A-Z0-9]*$", url)[0]

    filename = "retrieve_data.json"

    return registro


# Pages to scrap
num_offers = 1
print(f'Numero de ofertas: {num_offers}')

# List of urls
data_list = list()
for page in range(1, num_offers+1):
    offers = get_urls_empleos(page)
    for x in offers:
        print(f'Retrieving data from {x}')
        retrieved_dictionary = data_retrieval(x)
        data_list.append(retrieved_dictionary)
        actual_offer = JobOffer(**retrieved_dictionary)
        storage.new(actual_offer)
        storage.save()
        print('Saved to database')

with open("retrieve_data.json", "w+") as jsonfile:
    json.dump(data_list, jsonfile, ensure_ascii=False)
    print(f'PAGE {page} --- Data retrieval completed!')
