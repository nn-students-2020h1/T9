from content.utils import get_data


class Cat():
    IMAGE_URL = 'https://api.thecatapi.com/v1/images/search'
    FACT_URL = 'https://cat-fact.herokuapp.com/facts/random'

    @staticmethod
    def get_image():
        data = get_data(Cat.IMAGE_URL)
        if data:
            return data[0]["url"]

    @staticmethod
    def get_fact():
        data = get_data(Cat.FACT_URL)
        if data:
            return data['text']
