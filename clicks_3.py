import requests
from urllib.parse import urlparse,urlunparse

def shorten_link(token, url):
    header = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {"long_url": url}
    user_url = 'https://api-ssl.bitly.com/v4/bitlinks'

    response = requests.post(user_url, headers=header, json=payload)
    response.raise_for_status()
    short_link = response.json().get('id')
    return short_link


def count_clicks(token, link):
    header = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    user_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'

    response = requests.get(user_url, headers=header)
    response.raise_for_status()
    total_clicks = response.json().get('total_clicks')
    return total_clicks


def is_bitlink(url, token):
    try:
        if 'bit.ly' in url:
            parse_url = urlparse(url)
            if parse_url.scheme:
                parse_url = parse_url._replace(scheme='http')
                parse_url = urlunparse(url)
            total_clicks = count_clicks(token, url)
            print('Total clicks :', total_clicks)
        else:
            short_link = shorten_link(token, url)
            print('Your link :', short_link)
    except requests.exceptions.HTTPError as e:
        print('HTTP Error: ', e)


def main():
    token = 'dcffb0afddf1a77de9952b8aa11a29991883f591'
    url = input('Enter your url: ')
    is_bitlink(url, token)


main()
