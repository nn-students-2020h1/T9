from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

LEFTUPBUTTON = "callbackbuttonupleft"
RIGHTUPBUTTON = "callbackbuttonupright"
RIGHTDOWNBUTTON = "callbackbuttondownright"

TITLES = {
    LEFTUPBUTTON: "HISTORY",
    RIGHTUPBUTTON: "QUOTE",
    RIGHTDOWNBUTTON: "FACT"
}

def inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[LEFTUPBUTTON], callback_data=LEFTUPBUTTON),
            InlineKeyboardButton(TITLES[RIGHTUPBUTTON], callback_data=RIGHTUPBUTTON)
        ],
        [
            InlineKeyboardButton(TITLES[RIGHTDOWNBUTTON], callback_data=RIGHTDOWNBUTTON)
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

#in process
def keyboard_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data

    if data == LEFTUPBUTTON:
        return
    elif data == RIGHTUPBUTTON:
        return
    elif data == RIGHTDOWNBUTTON:
        return