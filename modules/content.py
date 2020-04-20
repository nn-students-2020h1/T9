import requests


def get_json(url):
    try:
        response = requests.get(url)

        if response.ok:
            data = response.json()
            return data

    except Exception as err:
        print(f'Error occurred: {err}')
        return None


class Cat():
    IMAGE_URL = 'https://api.thecatapi.com/v1/images/search'
    FACT_URL = 'https://cat-fact.herokuapp.com/facts/random'

    @staticmethod
    def get_image():
        data = get_json(Cat.IMAGE_URL)
        if data:
            return data[0]["url"]

    @staticmethod
    def get_fact():
        data = get_json(Cat.FACT_URL)
        if data:
            return data['text']


class CovidInfo:
    COUNTRY_TOP_URL = "https://bitlowsky-api.herokuapp.com/covid/country-top/"
    COUNTRY_DYNAMIC_TOP_URL = "https://bitlowsky-api.herokuapp.com/covid/country-dynamic-top/"
    PROVINCE_TOP_URL = "https://bitlowsky-api.herokuapp.com/covid/province-top/"
    PROVINCE_DYNAMIC_TOP_URL = "https://bitlowsky-api.herokuapp.com/covid/province-dynamic-top/"

    @staticmethod
    def get_country_top():
        return get_json(CovidInfo.COUNTRY_TOP_URL)

    @staticmethod
    def get_country_dynamic_top():
        return get_json(CovidInfo.COUNTRY_DYNAMIC_TOP_URL)

    @staticmethod
    def get_province_top():
        return get_json(CovidInfo.PROVINCE_TOP_URL)

    @staticmethod
    def get_province_dynamic_top():
        return get_json(CovidInfo.PROVINCE_DYNAMIC_TOP_URL)


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
