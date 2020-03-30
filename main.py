# -*- coding: utf-8 -*-
from telegram import Bot
from telegram.ext import (CallbackQueryHandler, CommandHandler, Filters,
                          MessageHandler, Updater)

from bot.Buttons1 import keyboard_callback
from bot.handlers import (chat_help, corono_stats, echo, error, history,
                          send_cat_fact, send_cat_image, send_quote, start,
                          stats_country)
from bot.log import logger
from bot.setup import PROXY, TOKEN


def main():
    bot = Bot(token=TOKEN, base_url=PROXY)
    updater = Updater(bot=bot, use_context=True)

    # on different commands - answer in Telegram
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', chat_help))
    updater.dispatcher.add_handler(CommandHandler('history', history))
    updater.dispatcher.add_handler(CommandHandler('quote', send_quote))
    updater.dispatcher.add_handler(CommandHandler('cat', send_cat_image))
    updater.dispatcher.add_handler(CommandHandler('fact', send_cat_fact))
    updater.dispatcher.add_handler(
        CommandHandler('corono_stats', corono_stats))
    updater.dispatcher.add_handler(
        CommandHandler('country_stats', stats_country))

    # keyboard
    updater.dispatcher.add_handler(CallbackQueryHandler(
        callback=keyboard_callback, pass_chat_data=True))
    # on noncommand i.e message - echo the message on Telegram
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    logger.info('Start Bot')
    main()
