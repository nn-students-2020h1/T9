from telegram import KeyboardButton, ReplyKeyboardMarkup

HELP = "/help"
HISTORY = "/history"

CAT_IMAGE = "/cat_image"
CAT_FACT = "/cat_fact"
MEME = "/meme"

COUNTRY_STATS = "/country_stats"
COUNTRY_DYNAMIC = "/country_dynamic"
PROVINCE_STATS = "/province_stats"
PROVINCE_DYNAMIC = "/province_dynamic"

MAIN_KEYBOARD = "/main"
COVID_KEYBOARD = "/covid"
CONTENT_KEYBOARD = "/content"


def main_keyboard():
    keyboard = [
        [
            KeyboardButton(HELP),
            KeyboardButton(HISTORY),
        ],
        [
            KeyboardButton(COVID_KEYBOARD),
            KeyboardButton(CONTENT_KEYBOARD),
        ],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def covid_keyboard():
    keyboard = [
        [
            KeyboardButton(COUNTRY_STATS),
            KeyboardButton(COUNTRY_DYNAMIC),
            KeyboardButton(PROVINCE_STATS),
            KeyboardButton(PROVINCE_DYNAMIC),
        ],
        [
            KeyboardButton(MAIN_KEYBOARD)
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def content_keyboard():
    keyboard = [
        [
            KeyboardButton(CAT_IMAGE),
            KeyboardButton(CAT_FACT),
            KeyboardButton(MEME)
        ],
        [
            KeyboardButton(MAIN_KEYBOARD)
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
