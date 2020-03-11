# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import CallbackContext
from bot.log import logger, log, ACTION_LOG
from modules.quote import get_quote

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

LEFTBUTTON = "callbackbuttonleft"
RIGHTBUTTON = "callbackbuttonright"

TITLES = {
    LEFTBUTTON: "HISTORY",
    RIGHTBUTTON: "QUOTE",
}

def inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[LEFTBUTTON], callback_data=LEFTBUTTON),
            InlineKeyboardButton(TITLES[RIGHTBUTTON], callback_data=RIGHTBUTTON)
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


@log
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        f'Привет, {update.effective_user.first_name}!\nСписок команд: /help')


@log
def chat_help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    msg = '''Команды:
    /start - начало
    /help - помощь
    /history - история действий
    /quote - случайная цитата'''
    update.message.reply_text(msg, reply_markup=inline_keyboard())


@log
def history(update: Update, context: CallbackContext):
    """Send a message when the command /history is issued."""

    # Get a list [{logs}] with user logs
    user_logs = [log for log in ACTION_LOG[update.effective_user['id']]]

    # Get a list of strings containing call and text attributes (see log.py)
    user_actions = [f'{act["call"]}:({act["text"]})' for act in user_logs][:5]

    # Convert the list of actions to a string separated by the Enter character
    msg = "Action history:\n    " + '\n    '.join(user_actions)
    update.message.reply_text(msg)


@log
def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


@log
def quote(update: Update, context: CallbackContext):
    quote, author, book, person = get_quote()
    msg = quote + '\n'

    if author:
        msg += f"\nАвтор: {author}"
    if book:
        msg += f"\nКнига: {book}"
    if person:
        msg += f"\nПерсонаж: {person}"

    update.message.reply_text(msg)


@log
def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')
