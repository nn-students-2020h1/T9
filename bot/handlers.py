# -*- coding: utf-8 -*-
from time import localtime, strftime

from telegram import Update
from telegram.ext import CallbackContext

from bot.keyboard import content_keyboard, covid_keyboard, main_keyboard
from bot.log import db, log, logger
from content.Cat import Cat
from content.CovidInfo import CovidInfo
from content.micro import get_image_tags, get_random_meme

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


@log
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        f'Hello, {update.effective_user.first_name}!', reply_markup=main_keyboard())


@log
def chat_help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    msg = 'The main commands are shown in the menu.\nYou can also send me an image so that I can try to recognize it.'

    update.message.reply_text(msg)


@log
def main_menu(update: Update, context: CallbackContext):
    """Send a message when the command /main is issued."""
    update.message.reply_text(
        'You are back in the main menu.', reply_markup=main_keyboard())


@log
def covid_menu(update: Update, context: CallbackContext):
    """Send a message when the command /covid is issued."""
    update.message.reply_text(
        "You have entered the covid menu.", reply_markup=covid_keyboard())


@log
def content_menu(update: Update, context: CallbackContext):
    """Send a message when the command /content is issued."""
    update.message.reply_text(
        "You have entered the content menu.", reply_markup=content_keyboard())


@log
def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


@log
def history(update: Update, context: CallbackContext):
    """Send a message when the command /history is issued."""
    userId = update.effective_user['id']

    logs = [log for log in db.logs.find({"userId": userId}, {
        "call": 1, 'message': 1, '_id': 0}).sort('time', -1).limit(5)]

    actions = '\n'.join([f"{log['call']}:({log['message']})" for log in logs])

    msg = f'''История запросов:\n{actions}'''
    update.message.reply_text(msg)


@log
def country_stats(update: Update, context: CallbackContext):
    current_date = strftime("%Y-%m-%d", localtime())

    data = db.covid.find_one({
        'type': 'country_stats',
        'date': current_date
    })

    if not data:
        data = CovidInfo.get_country_top()
        db.covid.insert_one({
            'type': 'country_stats',
            'data': data,
            'date': current_date
        })
    else:
        data = data['data']

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
    current_date = strftime("%Y-%m-%d", localtime())

    data = db.covid.find_one({
        'type': 'country_dynamic',
        'date': current_date
    })

    if not data:
        data = CovidInfo.get_country_dynamic_top(5)
        db.covid.insert_one({
            'type': 'country_dynamic',
            'data': data,
            'date': current_date
        })
    else:
        data = data['data']

    msg = "Country dynamic top:"

    for country in data:
        msg += f'\n{country["countryregion"]} ({country["lastdynamic"]} | {country["prevdynamic"]})'

    msg += "\n\nSee more on our website:\nhttps://bitlowsky.github.io/covid-19-info/"

    update.message.reply_text(msg)


@log
def province_stats(update: Update, context: CallbackContext):
    current_date = strftime("%Y-%m-%d", localtime())

    data = db.covid.find_one({
        'type': 'province_stats',
        'date': current_date
    })

    if not data:
        data = CovidInfo.get_province_top()
        db.covid.insert_one({
            'type': 'province_stats',
            'data': data,
            'date': current_date
        })
    else:
        data = data['data']

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
    current_date = strftime("%Y-%m-%d", localtime())

    data = db.covid.find_one({
        'type': 'province_dynamic',
        'date': current_date
    })

    if not data:
        data = CovidInfo.get_province_dynamic_top(5)
        db.covid.insert_one({
            'type': 'province_dynamic',
            'data': data,
            'date': current_date
        })
    else:
        data = data['data']

    msg = "Province dynamic top:"

    for province in data:
        msg += f'\n{province["provincestate"]}, {province["countryregion"]} ({province["lastdynamic"]} | {province["prevdynamic"]})'

    msg += "\n\nSee more on our website:\nhttps://bitlowsky.github.io/covid-19-info/"

    update.message.reply_text(msg)


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
def image_recognition(update: Update, context: CallbackContext):
    image_url = update.message.photo[-1].get_file().file_path
    msg = "На картинке:\n*" + "\n*".join(get_image_tags(image_url))
    update.message.reply_text(msg)


@log
def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')
