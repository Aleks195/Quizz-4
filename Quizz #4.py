import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

p = {'page': 1}
h = {'Accept-Language': 'en-US'}
url = 'https://www.myauto.ge/ka/s/0/0/41/00/00/00/00/00/iyideba-toyota?stype=0&for_rent=0&marka=41&currency_id=3&det_search=0&ord=7&keyword=&category_id=m0'

file = open('myauto.csv', 'w', encoding='UTF-8', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['carName','motor'])

while p['page']<6:
    r = requests.get(url, params=p, headers={'user-agent': 'Chrome'})
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    block = soup.find('div', class_='search-lists-container')
    all_autos = block.find_all('div', class_='current-item')

    for each in all_autos:
        carName = each.h4.a.text
        motor = each.find('div', class_='car-detail-in').text
        print(carName)
        file_obj.writerow([carName, motor])

    p['page'] += 1
    sleep(randint(14, 21))
file.close()