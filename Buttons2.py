from telegram import KeyboardButton, ReplyKeyboardMarkup

BUTTON_HISTORY = "HISTORY"
BUTTON_QUOTES = "QUOTES"
BUTTON_FACT = "FACT"
BUTTON_IMAGE = "IMAGE"

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