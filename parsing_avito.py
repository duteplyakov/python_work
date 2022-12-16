from bs4 import BeautifulSoup
import requests


product = input()

url = "https://www.avito.ru/rostov-na-donu?q=" + product
requests = requests.get(url)
bs = BeautifulSoup(requests.text, "html.parser")


all_link = bs.find_all("a", class_="iva-item-title-1Rmmj")

for link in all_link:
    print(link["href"])


