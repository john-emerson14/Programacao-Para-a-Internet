import requests


def main():
    imagem = requests.get("https://www.nautiljon.com/images/people/00/62/hatsune_miku_13626.jpg").content
    open('imagem.jpg', 'wb').write(imagem)


if __name__ == '__main__':
    main()
