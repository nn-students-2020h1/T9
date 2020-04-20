import random

import requests


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


def get_random_meme():
    # https://memasik.ru//memesimages/meme88157.jpg
    # методом перебора была найдена ссылка на последнюю картинку
    # было крайне сложно найти такой источник
    id = random.randint(1, 88157)
    return f"https://memasik.ru//memesimages/meme{id}.jpg"
