import requests
import bs4


def main():
    url = "http://www.google.com.br"
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, features="html.parser")
    links = lambda tag: getattr(tag, 'name', None) == 'a' and 'href' in tag.attrs
    results = soup.find_all(links)
    for link in results:
        print(link)


if __name__ == '__main__':
    main()
