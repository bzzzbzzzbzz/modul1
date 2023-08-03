import requests
from urllib.parse import urljoin

website_url = 'https://wttr.in/'
cities = {
    'London': { },
    'Аэропорт_Шереметьево': { },
    'череповец': {'lang': 'ru', 'M': '', 'n': '', 'q': '', 'T': ''}
}

for city, params in cities.items():
    url = urljoin(website_url, city)
    res = requests.get(url, params=params)
    res.raise_for_status()
    print(res.text)
