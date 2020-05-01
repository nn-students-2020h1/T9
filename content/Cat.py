import requests


class Cat():
    IMAGE_URL = 'https://api.thecatapi.com/v1/images/search'
    FACT_URL = 'https://cat-fact.herokuapp.com/facts/random'

    @staticmethod
    def get_image():
        try:
            response = requests.get(Cat.IMAGE_URL)

            if response.ok:
                return response.json()[0]["url"]

        except Exception:
            pass

        return "https://pro-training.com.ua/wp-content/uploads/2016/07/No1.jpg"

    @staticmethod
    def get_fact():
        try:
            response = requests.get(Cat.FACT_URL)

            if response.ok:
                return response.json()['text']

        except Exception:
            pass

        return "Information not found"
