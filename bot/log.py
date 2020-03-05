# -*- coding: utf-8 -*-
import logging
from time import localtime, strftime

# Enable logging
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO,
                    filename="bot.log", filemode='w')

logger = logging.getLogger(__name__)

# Dict for logging users actions
LOG_ACTIONS = {}


def log(function):
    def inner(*args, **kwargs):
        update = args[0]

        LOG = {
            "time": strftime("%Y-%m-%d %H:%M:%S", localtime()),
            "call": function.__name__,
            "user_id": update.effective_user['id'],
            "user_name": update.effective_user['username'],
            "user_first_name": update.effective_user['first_name'],
            "user_last_name": update.effective_user['last_name'],
            "text": update["message"]["text"]
        }

        # Logging a last 5 user actions
        if LOG_ACTIONS.get(LOG["user_id"]):
            LOG_ACTIONS[LOG["user_id"]].insert(0, LOG)
            if len(LOG_ACTIONS[LOG["user_id"]]) > 5:
                LOG_ACTIONS[LOG["user_id"]] = LOG_ACTIONS[LOG["user_id"]][:5]
        else:
            LOG_ACTIONS[LOG["user_id"]] = [LOG]

        # Create the string for a nice output view
        LOG_INFO = f"{LOG['call']}('{LOG['text']}') - user:[id: {LOG['user_id']} | username: {LOG['user_name']}({LOG['user_first_name']} {LOG['user_last_name']})]"
        print(LOG["time"], LOG_INFO)
        logger.info(LOG_INFO)

        return function(*args, **kwargs)
    return inner
