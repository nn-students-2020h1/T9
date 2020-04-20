# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import CallbackContext

from bot.keyboard import reply_keyboard
from bot.log import dataBase, log, logger
from modules.content import Cat, get_random_meme, CovidInfo

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
    /cat_image - картинка котика
    /cat_fact - популярный факт о котах
    /province_stats - топ 5 провинций по кол-ву заражённых
    /country_stats - топ 5 стран по кол-ву заражённых
    /meme - случайный мем (16+)
    /country_dynamic - динамика заражений по странам
    /province_dynamic - динамика заражений по регионам'''

    update.message.reply_text(msg)


@log
def country_stats(update: Update, context: CallbackContext):
    data = CovidInfo.get_country_top()
    lines = 0

    msg = "Latest info about the most infected countries:"
    for x in data:
        msg += f'\n{x["countryregion"]}: {x["confirmed"]}'
        lines += 1
        if lines == 5:
            break

    msg += "\n\nSee more on our website:\nhttps://bitlowsky.github.io/covid-19-info/"

    update.message.reply_text(msg)


@log
def country_dynamic(update: Update, context: CallbackContext):
    data = CovidInfo.get_country_dynamic_top()
    msg = "Country dynamic top:"

    for country in data:
        msg += f'\n{country["countryregion"]} ({country["lastdynamic"]} | {country["prevdynamic"]})'

    msg += "\n\nSee more on our website:\nhttps://bitlowsky.github.io/covid-19-info/"

    update.message.reply_text(msg)


@log
def province_stats(update: Update, context: CallbackContext):
    data = CovidInfo.get_province_top()
    lines = 0

    msg = "Latest info about the most infected provinces:"
    for x in data:
        msg += f'\n{x["provincestate"]}, {x["countryregion"]}: {x["confirmed"]}'
        lines += 1
        if lines == 5:
            break

    msg += "\n\nSee more on our website:\nhttps://bitlowsky.github.io/covid-19-info/"

    update.message.reply_text(msg)


@log
def province_dynamic(update: Update, context: CallbackContext):
    data = CovidInfo.get_province_dynamic_top()
    msg = "Province dynamic top:"

    for province in data:
        msg += f'\n{province["provincestate"]}, {province["countryregion"]} ({province["lastdynamic"]} | {province["prevdynamic"]})'

    msg += "\n\nSee more on our website:\nhttps://bitlowsky.github.io/covid-19-info/"

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
def cat_image(update: Update, context: CallbackContext):
    """Send a photo when the command /cat_image is issued."""
    update.message.reply_photo(Cat.get_image())


@log
def cat_fact(update: Update, context: CallbackContext):
    """Send a text when the command /cat_fact is issued."""
    update.message.reply_text(Cat.get_fact())


@log
def meme(update: Update, context: CallbackContext):
    """Send a photo when the command /meme is issued."""
    update.message.reply_photo(get_random_meme())


@log
def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')
