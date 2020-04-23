from content.utils import get_data


def get_random_meme():
    URL = "https://bitlowsky-api.herokuapp.com/meme/"
    data = get_data(URL)
    if data:
        return data


def get_image_tags(image_url):
    url = f"https://bitlowsky-api.herokuapp.com/image-recognition?url={image_url}"
    data = get_data(url)
    if data:
        return data["tags"]
