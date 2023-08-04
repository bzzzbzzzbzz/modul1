import requests
from urllib.parse import urljoin

website_url = 'https://wttr.in/'
site_params = {'lang': 'ru', 'M': '', 'n': '', 'q': '', 'T': ''}
cities = {
    'London': {},
    'Аэропорт_Шереметьево': {},
    'череповец': {},
}

for city, params in cities.items():
    city_params = {**site_params, **params}
    url = urljoin(website_url, city)
    res = requests.get(url, params=city_params)
    res.raise_for_status()
    print(res.text)
