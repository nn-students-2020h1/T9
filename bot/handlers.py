# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from bot.Buttons2 import reply_keyboard
from bot.log import dataBase, log, logger
from modules import content
from modules.CovidTable import CovidTable

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


@log
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        f'Привет, {update.effective_user.first_name}!\nСписок команд: /help', reply_markup=reply_keyboard())


@log
def chat_help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    msg = '''Команды:
    /start - начало
    /help - помощь
    /history - история действий
    /quote - случайная цитата
    /cat - картинка котика
    /fact - популярный факт о котах
    /province_stats - список 5 провинций, где больше всего новых заражённых
    /country_stats - список 5 стран, где больше всего новых заражённых'''

    update.message.reply_text(msg)


@log
def province_stats(update: Update, context: CallbackContext):
    table = CovidTable()
    date = table.get_table()
    info = table.get_confirmed_top("Province_State")[:5]

    msg = f"The most infected provinces on {date}:"

    for x in info:
        msg += f"\n{x[0]}:{x[1]}"

    update.message.reply_text(msg)


@log
def country_stats(update: Update, context: CallbackContext):
    table = CovidTable()
    date = table.get_table()
    info = table.get_confirmed_top("Country_Region")[:5]

    msg = f"The most infected provinces on {date}:"

    for x in info:
        msg += f"\n{x[0]}:{x[1]}"

    update.message.reply_text(msg)


@log
def history(update: Update, context: CallbackContext):
    """Send a message when the command /history is issued."""
    userId = update.effective_user['id']
    logs = dataBase.getRecords(
        'log', f"SELECT call, message FROM log WHERE userId={userId} ORDER BY time DESC", 5)
    actions = '\n'.join([f"{log[0]}:({log[1]})" for log in logs])

    msg = f'''История запросов:\n{actions}'''

    update.message.reply_text(msg)


@log
def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


@log
def send_quote(update: Update, context: CallbackContext):
    """Send a message when the command /quote is issued."""
    text, author, book, person = content.get_quote()
    msg = text + '\n'

    if author:
        msg += f"\nАвтор: {author}"
    if book:
        msg += f"\nКнига: {book}"
    if person:
        msg += f"\nПерсонаж: {person}"

    update.message.reply_text(msg)


@log
def send_cat_image(update: Update, context: CallbackContext):
    """Send a photo when the command /cat is issued."""
    update.message.reply_photo(content.get_cat_image())


@log
def send_cat_fact(update: Update, context: CallbackContext):
    """Send a text when the command /fact is issued."""
    update.message.reply_text(content.get_cat_fact())


@log
def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')
