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


def get_image_tags(image_url):
    ENTRY_POINT = "https://bitlowsky-api.herokuapp.com/image-recognition"
    url = ENTRY_POINT + f"?url={image_url}"
    data = get_json(url)
    if data:
        return data["tags"]
