import random

import requests
from bs4 import BeautifulSoup


class Cat():
    IMAGE_URL = 'https://api.thecatapi.com/v1/images/search'
    FACT_URL = 'https://cat-fact.herokuapp.com/facts/random'

    @staticmethod
    def get_image():
        try:
            response = requests.get(Cat.IMAGE_URL)
            if response.ok:
                data = response.json()
                return data[0]["url"]
        except Exception as err:
            print(f'Error occurred: {err}')

    @staticmethod
    def get_fact():
        try:
            response = requests.get(Cat.FACT_URL)
            if response.ok:
                data = response.json()
                return data['text']
        except Exception as err:
            print(f'Error occurred: {err}')


class Quote():
    URL = "https://icitaty.ru/random/"

    def __init__(self):
        self.get_random_quote()

    def get_random_quote(self):
        html = requests.get(Quote.URL).text
        soup = BeautifulSoup(html, "lxml")

        self.text = soup.find("p").text
        author = soup.find("a", attrs={"title": "Автор цитаты"})
        book = soup.find("a", attrs={"title": "Цитаты из книги"})
        person = soup.find("a", attrs={"title": "Цитируемый персонаж"})

        author = str(author)[str(author).find(
            "</i>") + 4:str(author).find("</a>")]
        book = str(book)[str(book).find("</i>") + 4:str(book).find("</a>")]
        person = str(person)[str(person).find(
            "</i>") + 4:str(person).find("</a>")]

        self.author = ' '.join(author.split())
        self.book = ' '.join(book.split())
        self.person = ' '.join(person.split())

    def get_text(self):
        msg = self.text + '\n'

        if self.author:
            msg += f"\nАвтор: {self.author}"
        if self.book:
            msg += f"\nКнига: {self.book}"
        if self.person:
            msg += f"\nПерсонаж: {self.person}"

        return msg

    def __str__(self):
        return self.get_text()


def get_random_meme():
    # https://memasik.ru//memesimages/meme88157.jpg
    # методом перебора была найдена ссылка на последнюю картинку
    # было крайне сложно найти такой источник
    id = random.randint(1, 88157)
    return f"https://memasik.ru//memesimages/meme{id}.jpg"
