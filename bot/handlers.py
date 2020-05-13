# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

import content.messages as message
from bot.keyboard import (content_keyboard, covid_keyboard,
                          image_recognition_keyboard, main_keyboard,
                          weather_keyboard)
from bot.log import log, logger
from content.Cat import Cat
from content.utils import (get_image_tags_with_db_check, get_last_image_url,
                           get_meme_url, set_last_image_url)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


@log
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text(f'Hello, {update.effective_user.first_name}!', reply_markup=main_keyboard())


@log
def chat_help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'The main commands are shown in the menu.\nYou can also send me an image so that I can try to recognize it.')


@log
def main_menu(update: Update, context: CallbackContext):
    """Send a message when the command /main is issued."""
    update.message.reply_text('You are back in the main menu.', reply_markup=main_keyboard())
    return ConversationHandler.END


@log
def covid_menu(update: Update, context: CallbackContext):
    """Send a message when the command /covid is issued."""
    update.message.reply_text("You have entered the covid menu.", reply_markup=covid_keyboard())


@log
def content_menu(update: Update, context: CallbackContext):
    """Send a message when the command /content is issued."""
    update.message.reply_text("You have entered the content menu.", reply_markup=content_keyboard())


@log
def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


@log
def history(update: Update, context: CallbackContext):
    """Send a message when the command /history is issued."""
    update.message.reply_text(message.history(update.effective_user['id']))


@log
def country_stats(update: Update, context: CallbackContext):
    """Send a photo when the command /country_stats is issued."""
    query = update.message.text

    if query == "/country_stats":
        update.message.reply_text('Enter the date in the format DAY-MONTH-YEAR or send /latest')
        return 1

    elif query == '/latest':
        update.message.reply_text(message.covid('country_stats', 5))

    else:
        update.message.reply_text(message.covid('country_stats', 5, query))

    return ConversationHandler.END


@log
def country_dynamic(update: Update, context: CallbackContext):
    """Send a photo when the command /country_dynamic is issued."""
    update.message.reply_text(message.covid('country_dynamic', 5))


@log
def province_stats(update: Update, context: CallbackContext):
    """Send a photo when the command /province_stats is issued."""
    update.message.reply_text(message.covid('province_stats', 5))


@log
def province_dynamic(update: Update, context: CallbackContext):
    """Send a photo when the command /province_dynamic is issued."""
    update.message.reply_text(message.covid('province_dynamic', 5))


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
    update.message.reply_photo(get_meme_url())


@log
def image_recognition(update: Update, context: CallbackContext):
    user_id = update['_effective_user']['id']
    image_url = get_last_image_url(user_id)

    query = update.message.text

    if not query:
        image_url = update.message.photo[-1].get_file().file_path
        set_last_image_url(user_id, image_url)
        update.message.reply_text('Select the option.', reply_markup=image_recognition_keyboard())
        return 1

    elif query == 'tags':
        tags = get_image_tags_with_db_check(image_url)
        update.message.reply_text(message.image_recognition(tags), reply_markup=main_keyboard())

    elif query == 'wiki':
        tags = get_image_tags_with_db_check(image_url)
        update.message.reply_text(message.wiki_info(tags[0]), reply_markup=main_keyboard())

    return ConversationHandler.END


@log
def wiki(update: Update, context: CallbackContext):
    """Send a photo when the command /wiki is issued."""
    query = update.message.text

    if query == "/wiki":
        update.message.reply_text('What would you like to know?')
        return 1

    else:
        update.message.reply_text(message.wiki_info(query))

    return ConversationHandler.END


@log
def currency_rates(update: Update, context: CallbackContext):
    """Send a message when the command /currency_rates is issued."""
    update.message.reply_text(message.currency_rates())


@log
def weather(update: Update, context: CallbackContext):
    """Send a message when the command /weather is issued."""
    query = update.message.text

    if query == '/weather':
        update.message.reply_text('Select this option or enter the number of days manually.', reply_markup=weather_keyboard())
        return 1

    elif query == 'all':
        update.message.reply_text(message.weather(), reply_markup=main_keyboard())

    else:
        update.message.reply_text(message.weather(int(query)), reply_markup=main_keyboard())

    return ConversationHandler.END


@log
def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')
