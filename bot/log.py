# -*- coding: utf-8 -*-
import logging
from time import localtime, strftime
import pickle


# Enable logging
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO,
                    filename="bot.log", filemode='w')

logger = logging.getLogger(__name__)


def load_logs():
    '''Load users actions log from pickle file'''
    try:
        with open("log.pickle", "rb") as f:
            ACTION_LOG = pickle.load(f)
    except:
        ACTION_LOG = {}
    finally:
        return ACTION_LOG


def dump_logs():
    '''Dump users actions to pickle file'''
    with open('log.pickle', 'wb') as f:
        pickle.dump(ACTION_LOG, f)


# Dict for logging users actions
ACTION_LOG = load_logs()
print(len(ACTION_LOG), "user logs has been loaded")


def log(function):
    def inner(*args, **kwargs):
        update = args[0]
        USER_ID = update.effective_user['id']
        USER_NAME = update.effective_user['username']

        USER_ACTION = {
            "time": strftime("%Y-%m-%d %H:%M:%S", localtime()),
            "call": function.__name__,
            "text": update["message"]["text"]
        }

        # Logging user actions
        if ACTION_LOG.get(USER_ID):
            ACTION_LOG[USER_ID].insert(0, USER_ACTION)
        else:
            ACTION_LOG[USER_ID] = [USER_ACTION]

        # Create the string for a nice output view
        LOG_INFO = f'user:[{USER_ID} ({USER_NAME})] - call:[{USER_ACTION["call"]}("{USER_ACTION["text"]}")]'
        print(USER_ACTION["time"], LOG_INFO)
        logger.info(LOG_INFO)

        return function(*args, **kwargs)
    return inner
