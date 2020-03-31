from telegram import KeyboardButton, ReplyKeyboardMarkup

BUTTON_HISTORY = "/history"
BUTTON_QUOTES = "/quote"
BUTTON_FACT = "/cat_fact"
BUTTON_IMAGE = "/cat_image"
BUTTON_HELP = "/help"
BUTTON_CORONA_STATUS = "/province_stats"
BUTTON_COUNTRY_STATUS = "/country_stats"


def reply_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON_HELP)
        ],
        [
            KeyboardButton(BUTTON_CORONA_STATUS),
            KeyboardButton(BUTTON_COUNTRY_STATUS)
        ],
        [
            KeyboardButton(BUTTON_HISTORY),
            KeyboardButton(BUTTON_QUOTES),
        ],
        [
            KeyboardButton(BUTTON_FACT),
            KeyboardButton(BUTTON_IMAGE),
        ],
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )
