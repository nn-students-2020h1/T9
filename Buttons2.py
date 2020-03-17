from telegram import KeyboardButton, ReplyKeyboardMarkup

BUTTON_HISTORY = "HISTORY"
BUTTON_QUOTES = "QUOTES"
BUTTON_FACT = "FACT"

def reply_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON_HISTORY),
            KeyboardButton(BUTTON_QUOTES),
            KeyboardButton(BUTTON_FACT),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )