# -*- coding: utf-8 -*-
import logging
from time import localtime, strftime

import pymongo

# Enable logging
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO,
                    filename="bot.log", filemode='w')

logger = logging.getLogger(__name__)

# Initialize MongoDB and log_history collection
client = pymongo.MongoClient("localhost", 27017)
db = client.T9_bot
log_history = db.log


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
        log_history.insert_one(DATA)

        # Create the string for a nice output view
        LOG_INFO = f'user:[{DATA["userId"]} ({DATA["userName"]})] - call:[{DATA["call"]}("{DATA["message"]}")]'
        logger.info(LOG_INFO)
        print(DATA["time"], LOG_INFO)

        return function(*args, **kwargs)
    return inner
