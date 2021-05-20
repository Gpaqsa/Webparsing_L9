import requests
from bs4 import BeautifulSoup

lp = open("laptops.csv", 'w')
headings = 'Title\n'
lp.write(headings)


url = "https://www.ebay.com/b/Xiaomi-PC-Laptops-Netbooks/177/bn_7109864258"
connect = requests.get(url)
print(connect.status_code)
# print(connect.text)
content = connect.text
soup = BeautifulSoup(content, 'html.parser')

ul = soup.find('ul', {'class': 'b-list__items_nofooter srp-results srp-grid'})
# print(ul)
all_laptops = ul.find_all('li')
# print(all_laptops)


for laptops in all_laptops:
    info = laptops.find('div', {'class': "s-item__wrapper clearfix"})
    title_bar = info.find('div', {'class': "s-item__info clearfix"})
    # title = title_bar.find('h3', {'class': "s-item__title"})
    title = title_bar.a.h3.text.strip()
    url = title_bar.a['href']
    print(title)
    lp.write(title+'\n')


