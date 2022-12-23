from bs4 import BeautifulSoup
import requests

# apple_hpone_url = 'https://asaxiy.uz/uz/product?key=apple+phone'

# r = requests.get(apple_hpone_url)

with open('phone.html', 'r', encoding='UTF8') as f:
    text = f.read()

soup = BeautifulSoup(text, features='html.parser')

print(type(soup.find_all('p', attrs={'class':'title__link'})))