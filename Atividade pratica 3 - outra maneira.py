import requests
from bs4 import BeautifulSoup


def main():
    response = requests.get('http://www.google.com.br')

    html = BeautifulSoup(response.text, 'html.parser')
    links = html.find_all('a')
    for link in links:
        print(link['href'])


if __name__ == '__main__':
    main()
