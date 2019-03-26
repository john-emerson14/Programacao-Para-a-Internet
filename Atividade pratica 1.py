import requests


def main():
    url = input('Url: ')
    response = requests.get(url)
    print("Status code:", response.status_code)
    print("Cabeçalhos (response headers):", response.headers)
    print("Tamanho da resposta (content length):", response.headers['content-length'])
    print("Corpo da resposta:", response.text)


if __name__ == '__main__':
    main()
