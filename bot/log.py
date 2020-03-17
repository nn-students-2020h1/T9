# -*- coding: utf-8 -*-
import logging
from time import localtime, strftime

from modules.sql import SqlDataBase

# Enable logging
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO,
                    filename="bot.log", filemode='w')

logger = logging.getLogger(__name__)

dataBase = SqlDataBase("telegram.db", check_thread=False)
if 'log' not in dataBase.tables:
    fields = '''
    userId integer,
    userName text,
    call text,
    message text,
    time text
    '''
    dataBase.createTable('log', fields)


# Decorator
def log(function):
    def inner(*args, **kwargs):
        update = args[0]

        DATA = {
            "userId": update.effective_user['id'],
            "userName": update.effective_user['username'],
            "call": function.__name__,
            "message": update["message"]["text"],
            "time": strftime("%Y-%m-%d %H:%M:%S", localtime())
        }

        # Create the string for a nice output view
        LOG_INFO = f'user:[{DATA["userId"]} ({DATA["userName"]})] - call:[{DATA["call"]}("{DATA["message"]}")]'
        logger.info(LOG_INFO)
        print(DATA["time"], LOG_INFO)

        # Logging user actions
        dataBase.addRecord("log", DATA)

        return function(*args, **kwargs)
    return inner
