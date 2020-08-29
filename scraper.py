import requests
from bs4 import BeautifulSoup

URL = 'https://www.jumia.co.ke/samsung-galaxy-a10s-6.2-4g-32gb-2gb-dual-sim-blue.-22893932.html'

headers = {
    'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('h1', {'class': '-fs20'}).get_text()
    price = soup.find('span', {'class': '-tal'}).get_text()
    converted_price = float(''.join(price.split(' ')[1].split(',')))

    if converted_price < 12000:
        send_mail()
