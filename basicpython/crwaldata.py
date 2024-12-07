import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")
print(soup)
boxes = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
# print(boxes)
print(len(boxes))
names = soup.find_all("a", class_="title")
for i in names:
    print(i.text)

price = soup.find_all("h4", class_="price float-end card-title pull-right")
print(len(price))
for j in price:
    print(j.text)

review_count = soup.find_all("p", class_="review-count float-end")
for k in review_count:
    print(k.text)

description_item = soup.find_all("p", class_="description card-text")
for z in description_item:
    print(z.text)
