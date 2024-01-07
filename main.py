from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
   
   
my_url = 'https://krisha.kz/prodazha/kvartiry/talgar/?page=1'
# here I could use for loop instead of changing pages from 1 to 2 and so on ,but it took too long ,so I created 16 csvs and then added them in one csv
uclient = uReq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div", {"class":"a-card__main-info"})
containers2 = page_soup.findAll("div", {"class":"a-card__wrapper-subtitle"})

file_name = "houses1.csv"
f = open(file_name, "w",encoding='utf-8')

headers = "location,price,room,area\n"
f.write(headers)
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
# try:
#     uclient = uReq(my_url)
#     # Rest of your code
# except TimeoutError as e:
#     print(f"TimeoutError: {e}")
#     # Handle the error as needed (e.g., retry, skip, or exit the script)
# uclient = uReq(my_url, timeout=10)  # Adjust the timeout value as needed
