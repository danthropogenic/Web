# practicepython.org exercise 17: decode a web page

# print a list of NY times article headlines

import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com"
nyt = requests.get(url)
nyt_html = nyt.text
soup = BeautifulSoup(nyt_html,"html.parser")
for article in soup.find_all(class_="story-heading"):
    print(article.get_text().replace("\n"," ").strip())
