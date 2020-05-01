import requests


def get_random_meme():
    URL = "https://bitlowsky-api.herokuapp.com/meme/"

    try:
        response = requests.get(URL)

        if response.ok:
            return response.text

    except Exception:
        return "https://pro-training.com.ua/wp-content/uploads/2016/07/No1.jpg"


def get_image_tags(image_url):
    url = f"https://bitlowsky-api.herokuapp.com/image-recognition?url={image_url}"

    try:
        response = requests.get(url)

        if response.ok:
            return response.json()['tags']

    except Exception:
        return []
