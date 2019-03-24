# -*- coding: utf-8 -*-
import requests


def main():
    response = requests.get('http://www.google.com')
    print("Status code:", response.status_code)
    print("Cabeçalhos (response headers):", response.headers)
    print("Tamanho da resposta (content length):", response.headers['content-length'])
    print("Corpo da resposta:", response.text)


if __name__ == '__main__':
    main()
