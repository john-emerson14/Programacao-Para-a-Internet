import requests
import bs4


def main():
    url = "https://www.google.com.br"
    html_page = requests.get(url).content
    soup = bs4.BeautifulSoup(html_page, features="html.parser")

    links = [link['href'] for link in soup('a') if 'href' in link.attrs]

    for link in links:
        print(link)


if __name__ == '__main__':
    main()
