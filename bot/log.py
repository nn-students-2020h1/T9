# -*- coding: utf-8 -*-
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

LOG_ACTIONS = []


def log(function):
    def inner(*args, **kwargs):
        update = args[0]
        i = len(LOG_ACTIONS)
        LOG_ACTIONS.append({
            "date": update["message"]["date"],
            "call": function.__name__,
            "user": update.effective_user,
            "text": update["message"]["text"]
        })
        print(
            f"{LOG_ACTIONS[i]['date']} |",
            f"call: {LOG_ACTIONS[i]['call']} |",
            f"id: {LOG_ACTIONS[i]['user']['id']} |",
            f"user: {LOG_ACTIONS[i]['user']['username']}",
            f"({LOG_ACTIONS[i]['user']['first_name']}",
            f"{LOG_ACTIONS[i]['user']['last_name']}) |",
            f"text: {LOG_ACTIONS[i]['text']}"
        )
        return function(*args, **kwargs)
    return inner
