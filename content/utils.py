import re
from random import randint
from urllib.request import urlopen

import imagehash
import requests
import wikipedia
from fuzzywuzzy import process
from PIL import Image

from bot.setup import db


def get_meme_url(meme_id: int = None, depth=10) -> str:
    if depth == 0:
        return ''

    meme_id = meme_id if meme_id else randint(1, 100000)
    meme_url = f"https://memasik.ru/memesimages/meme{meme_id}.jpg"
    response = requests.get(meme_url)

    if response.text == 'false':
        return get_meme_url(depth=depth-1)

    return meme_url


def get_image_hash(image_url: str):
    return imagehash.average_hash(Image.open(urlopen(image_url)))


def get_image_tags(image_url):
    url = f"https://bitlowsky-api.herokuapp.com/image-recognition?url={image_url}"

    try:
        response = requests.get(url)

        if response.ok:
            return response.json()['tags']

    except Exception:
        pass

    return []


def get_history(user_id, count):
    return list(db.logs.find({"userId": user_id}, {"call": 1, 'message': 1, 'time': 1, '_id': 0}).sort('time', -1).limit(5))


def format_date(date):
    res = re.findall(r"(0?[1-9]|[12][0-9]|3[01])[\- ./](0?[1-9]|1[012])[\- ./](20[0-9]{2}|[0-9]{4}|[0-9]{2})", date)

    try:
        day, month, year = res[0]
        day = day[1] if day[0] == '0' else day
        month = month[1] if month[0] == '0' else month
        year = year[-2:]

        return f'{month}/{day}/{year}'

    except Exception:
        return ''


def get_wiki_summary(query: str, lang: str = 'ru') -> str:
    wikipedia.set_lang(lang)
    options = wikipedia.search(query)

    for word in query.split():
        options += wikipedia.search(word)

    try:
        nearest, _ = process.extractOne(query, set(options))
        return wikipedia.summary(nearest)

    except Exception:
        raise Exception('Information not found. Try again.')


def get_wiki_summary_with_db_check(query):
    data = db.wiki.find_one({'query': query})

    if data:
        return data['summary']

    else:
        try:
            summary = get_wiki_summary(query)
            db.wiki.insert_one({'query': query, 'summary': summary})
            return summary

        except Exception as err:
            print(err)
