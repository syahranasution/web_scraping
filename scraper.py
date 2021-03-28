import requests 
from bs4 import BeautifulSoup

url = "https://belajarpython.com/tutorial/object-class-python"

r = requests.get(url)

soup = BeautifulSoup(r.content, features="html.parser")

titles = soup.findAll("h3")

# comment apa blabla
for title in titles:
    print(title.text)