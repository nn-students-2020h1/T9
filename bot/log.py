# -*- coding: utf-8 -*-
import logging
from time import localtime, strftime

from bot.setup import db

# Enable logging
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'

file_log = logging.FileHandler('bot.log')
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(file_log, console_out),
                    format=LOG_FORMAT, level=logging.INFO)

logger = logging.getLogger(__name__)


# log decorator
def log(function):
    def inner(*args, **kwargs):
        update = args[0]

        DATA = {
            "userId": update['_effective_user']['id'],
            "userName": update['_effective_user']['username'],
            "call": function.__name__,
            "message": update["message"]["text"],
            "time": strftime("%Y-%m-%d %H:%M:%S", localtime())
        }

        # Logging user actions
        db.logs.insert_one(DATA)

        # Create the string for a nice output view
        LOG_INFO = f'user:[{DATA["userId"]} ({DATA["userName"]})] - call:[{DATA["call"]}("{DATA["message"]}")]'
        logger.info(LOG_INFO)

        return function(*args, **kwargs)
    return inner
