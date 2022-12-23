from bs4 import BeautifulSoup

with open('home.html', 'r') as f:
    text = f.read()

soup = BeautifulSoup(text, features="html.parser")

print(soup.find_next_sibling('h1'))