# -*- coding: utf-8 -*-
import requests


def main():
    imagem = requests.get("https://www.bestservice.com/img_share/image/Products/Crypton/2D_miku_V4X.jpg").content
    open('imagem.jpg', 'wb').write(imagem)


if __name__ == '__main__':
    main()
