import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.jumia.co.ke/samsung-galaxy-a10s-6.2-4g-32gb-2gb-dual-sim-blue.-22893932.html'

headers = {
    'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('h1', {'class': '-fs20'}).get_text()
    price = soup.find('span', {'class': '-tal'}).get_text()
    converted_price = float(''.join(price.split(' ')[1].split(',')))

    if converted_price < 11000:
        send_mail()
    else:
        print('PRICE HAS NOT CHANGED')


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('nakolahdaniel1@gmail.com', 'jltxloxagtmqoqmh')

    subject = 'Price fell down!'
    body = f'Check the Jumia link {URL}'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'nakolahdaniel1@gmail.com',
        'nakolahdaniel1@gmail.com',
        msg
    )
    print('HEY! EMAIL HAS BEEN SENT')
    server.quit()


if __name__ == "__main__":
    while True:
        try:
            check_price()
            time.sleep(60*60)
        except KeyboardInterrupt:
            print(' pressed, exiting...')
            break
