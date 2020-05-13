from telegram import KeyboardButton, ReplyKeyboardMarkup

HELP = "/help"
HISTORY = "/history"

CAT_IMAGE = "/cat_image"
CAT_FACT = "/cat_fact"
MEME = "/meme"
WIKI = '/wiki'

COUNTRY_STATS = "/country_stats"
COUNTRY_DYNAMIC = "/country_dynamic"
PROVINCE_STATS = "/province_stats"
PROVINCE_DYNAMIC = "/province_dynamic"

MAIN_KEYBOARD = "/main"
COVID_KEYBOARD = "/covid"
CONTENT_KEYBOARD = "/content"
CURRENCY_RATES = "/currency_rates"
WEATHER = "/weather"


def main_keyboard():
    keyboard = [
        [
            KeyboardButton(HELP),
            KeyboardButton(HISTORY),
            KeyboardButton(CURRENCY_RATES),
        ],
        [
            KeyboardButton(COVID_KEYBOARD),
            KeyboardButton(WIKI),
            KeyboardButton(WEATHER),
            KeyboardButton(CONTENT_KEYBOARD),
        ],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def covid_keyboard():
    keyboard = [
        [
            KeyboardButton(COUNTRY_STATS),
            KeyboardButton(COUNTRY_DYNAMIC),
        ],
        [
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


def image_recognition_keyboard():
    keyboard = [
        [
            KeyboardButton('tags'),
            KeyboardButton('wiki')
        ],
        [
            KeyboardButton(MAIN_KEYBOARD)
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def weather_keyboard():
    keyboard = [
        [
            KeyboardButton('3'),
            KeyboardButton('7'),
            KeyboardButton('all'),
        ],
        [
            KeyboardButton(MAIN_KEYBOARD)
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
