# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

import content.messages as message
from bot.keyboard import content_keyboard, covid_keyboard, main_keyboard
from bot.log import log, logger
from content.Cat import Cat
from content.utils import get_meme_url

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
    update.message.reply_text(
        'The main commands are shown in the menu.\nYou can also send me an image so that I can try to recognize it.')


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
    image_url = update.message.photo[-1].get_file().file_path
    update.message.reply_text(message.image_recognition(image_url))


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
def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')
