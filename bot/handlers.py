# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import CallbackContext
from bot.log import logger, log, ACTION_LOG

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


@log
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text(f'Привет, {update.effective_user.first_name}!')


@log
def chat_help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Введи команду /start для начала. ')


@log
def history(update: Update, context: CallbackContext):
    """Send a message when the command /history is issued."""

    # Get a list [{logs}] with user logs
    user_logs = [log for log in ACTION_LOG[update.effective_user['id']]]

    # Get a list of strings containing call and text attributes (see log.py)
    user_actions = [f'{act["call"]}:({act["text"]})' for act in user_logs][:5]

    # Convert the list of actions to a string separated by the Enter character
    msg = "Action history:\n" + '\n'.join(user_actions)
    update.message.reply_text(msg)


@log
def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


@log
def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')
