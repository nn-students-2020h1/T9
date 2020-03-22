from telegram import KeyboardButton, ReplyKeyboardMarkup

BUTTON_HISTORY = "/history"
BUTTON_QUOTES = "/quote"
BUTTON_FACT = "/fact"
BUTTON_IMAGE = "/cat"


def reply_keyboard():
    keyboard = [
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