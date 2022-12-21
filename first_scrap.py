import requests


r = requests.get('https://example.com/')

print(r.text.split('<h1>')[1].split('</h1>')[0])