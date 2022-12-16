from bs4 import BeautifulSoup
import requests

product = input("Введи слово")
url = "https://www.avito.ru/rostov-na-donu?q=" + product
request = requests.get(url)
bs = BeautifulSoup(request.text, "html.parser")

all_links = bs.find_all("a", class_="iva-item-title-1Rmmj")

for link in all_links:
    print("https://www.avito.ru/" + link["href"])

