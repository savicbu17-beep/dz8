import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url, verify=False, timeout=3)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("h3 a")

for i, b in enumerate(books[:10]):
    print(i, b["title"])