# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import CallbackContext

from Buttons1 import inline_keyboard
from Buttons2 import BUTTON_HISTORY, BUTTON_QUOTES, BUTTON_FACT
from bot.log import logger, log, ACTION_LOG
from modules.quote import get_quote
import requests
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

def fact(update: Update, context: CallbackContext):
    r = requests.get('https://cat-fact.herokuapp.com/facts')
    dict = r.json()['all']
    likes = 0
    fact = ''
    for Value in dict:
        if (Value['upvotes']) > likes:
            likes = Value['upvotes']
            fact = Value['text']
    update.message.reply_text(fact)

@log
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        f'Привет, {update.effective_user.first_name}!\nСписок команд: /help'
    )

@log
def chat_help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    msg = '''Команды:
    /start - начало
    /help - помощь
    /history - история действий
    /quote - случайная цитата
    /fact - самый залайканный факт'''
    update.message.reply_text(msg, reply_markup=inline_keyboard())


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
    if update.message.text == BUTTON_HISTORY:
        return history(update=update, context=context)
    if update.message.text == BUTTON_QUOTES:
        return quote(update=update, context=context)
    if update.message.text == BUTTON_FACT:
        return fact(update=update, context=context)
    """Echo the user message."""
    update.message.reply_text(update.message.text)

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
