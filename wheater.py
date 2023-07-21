import requests

cities = ['London', 'Аэропорт_Шереметьево', 'череповец?lang=ru&?M&?n&?q&?T']

for city in cities:
    url = 'https://wttr.in/{}'
    res = requests.get(url.format(city))
    res.raise_for_status()
    print(res.text)
