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
    URL = "https://bitlowsky-api.herokuapp.com/meme/"
    try:
        response = requests.get(URL)

        if response.ok:
            return response.text

        else:
            return "Не сегодня..."

    except Exception as err:
        print(f'Error occurred: {err}')
