import requests 
from bs4 import BeautifulSoup

url = "https://belajarpython.com/tutorial/object-class-python"

r = requests.get(url)

soup = BeautifulSoup(r.content, features="html.parser")

# ambil semua title materi
titles = soup.findAll("h3")

for title in titles:
    print(title.text)