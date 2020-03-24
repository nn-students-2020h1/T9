from telegram import KeyboardButton, ReplyKeyboardMarkup

BUTTON_HISTORY = "request history"
BUTTON_QUOTES = "quote"
BUTTON_FACT = "fact about cats"
BUTTON_IMAGE = "cat photo"
BUTTON_HELP = "help"
BUTTON_CORONA_STATUS = " highest infection rate"
BUTTON_COUNTRY_STATUS = "most infected country"


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