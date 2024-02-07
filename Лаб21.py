import requests
from bs4 import BeautifulSoup
import csv

url = "https://tb.by/individuals/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
items = soup.find_all("tr")
print(items)
courses = []

for item in items:
    print(item)
    _item = item.find_all("td")
    courses.append({
        'units_column': _item[0].get_text(),
        'currency-media-new-curr1': _item[1].get_text(),
        'currency-media-new-curr2': _item[2].get_text().strip()
    })
print(courses)

with open('curs1.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=['units_column', 'currency-media-new-curr1', 'currency-media-new-curr2'],
        delimiter=';',
        quoting=csv.QUOTE_MINIMAL
    )
    writer.writeheader()
    for elem in courses:
        writer.writerow(elem)