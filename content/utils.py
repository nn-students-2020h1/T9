import re

from bot.setup import db


def get_history(user_id, count):
    return list(db.logs.find({"userId": user_id}, {"call": 1, 'message': 1, 'time': 1, '_id': 0}).sort('time', -1).limit(5))


def format_date(date):
    res = re.findall(r"(0?[1-9]|[12][0-9]|3[01])[\- ./](0?[1-9]|1[012])[\- ./](20[0-9]{2}|[0-9]{4}|[0-9]{2})", date)
    day = res[0][0].replace('0', '')
    month = res[0][1].replace('0', '')
    year = res[0][2][-2:]

    return f'{month}/{day}/{year}'
