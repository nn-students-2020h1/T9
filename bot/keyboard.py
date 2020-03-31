from telegram import KeyboardButton, ReplyKeyboardMarkup

BUTTON_HELP = "/help"
BUTTON_HISTORY = "/history"
BUTTON_QUOTE = "/quote"
BUTTON_CAT_FACT = "/cat_fact"
BUTTON_CAT_IMAGE = "/cat_image"
BUTTON_MEME = "/meme"
BUTTON_PROVINCE_STATS = "/province_stats"
BUTTON_COUNTRY_STATS = "/country_stats"


def reply_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON_HELP),
            KeyboardButton(BUTTON_HISTORY),
            KeyboardButton(BUTTON_QUOTE),
        ],
        [
            KeyboardButton(BUTTON_COUNTRY_STATS),
            KeyboardButton(BUTTON_PROVINCE_STATS),
        ],
        [
            KeyboardButton(BUTTON_CAT_IMAGE),
            KeyboardButton(BUTTON_CAT_FACT),
            KeyboardButton(BUTTON_MEME),
        ],
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )
