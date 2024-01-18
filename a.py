from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

file_name = "houses.csv"
f = open(file_name, "w",encoding='utf-8')

headers = "location,price,room,area\n"
f.write(headers)
for i in range(1,17):
    my_url = f'https://krisha.kz/prodazha/kvartiry/talgar/?page={i}'
# here I could use for loop instead of changing pages from 1 to 2 and so on ,but it took too long ,so I created 16 csvs and then added them in one csv
    uclient = uReq(my_url)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html,"html.parser")

    containers = page_soup.findAll("div", {"class":"a-card__main-info"})
    containers2 = page_soup.findAll("div", {"class":"a-card__wrapper-subtitle"})
    for container, container2 in zip(containers, containers2):
        house_info = []
        location = container2.find('div', {"class": {"a-card__subtitle"}}).text
        description = container.find('a', {"class": {"a-card__title"}}).text
        location = location.strip()
        location_parts = location.split(',')
        location = location_parts[0]
        room=description[0]
        area=description[22:25]
        price = container.find('div', {"class": "a-card__price"}).text
        price = price.replace('\n', '')
        price = price.replace(' ', '')
        price = price.replace('от', '')
        price = price.replace('&nbsp', '')
        price = price.replace('\xa0', '')
        price = price.replace('〒', '')

        house_info.append(location)
        house_info.append(price)

        house_info.append(room)
        house_info.append(area)
        f.write(','.join(map(str, house_info)) + "\n")
f.close()
