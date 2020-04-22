# -*- coding: utf-8 -*-
from telegram import Bot
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from bot.handlers import (cat_fact, cat_image, chat_help, content_menu,
                          country_dynamic, country_stats, covid_menu, echo,
                          error, history, image_recognition, main_menu, meme,
                          province_dynamic, province_stats, start)
from bot.log import logger
from bot.setup import PROXY, TOKEN


def main():
    bot = Bot(token=TOKEN, base_url=PROXY)
    updater = Updater(bot=bot, use_context=True)

    # on different commands - answer in Telegram
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', chat_help))
    updater.dispatcher.add_handler(CommandHandler('history', history))

    updater.dispatcher.add_handler(CommandHandler('main', main_menu))
    updater.dispatcher.add_handler(CommandHandler('covid', covid_menu))
    updater.dispatcher.add_handler(CommandHandler('content', content_menu))

    updater.dispatcher.add_handler(CommandHandler('cat_image', cat_image))
    updater.dispatcher.add_handler(CommandHandler('cat_fact', cat_fact))
    updater.dispatcher.add_handler(CommandHandler('meme', meme))

    updater.dispatcher.add_handler(
        CommandHandler('country_stats', country_stats))
    updater.dispatcher.add_handler(
        CommandHandler('country_dynamic', country_dynamic))
    updater.dispatcher.add_handler(
        CommandHandler('province_stats', province_stats))
    updater.dispatcher.add_handler(
        CommandHandler('province_dynamic', province_dynamic))

    # on noncommand i.e message - echo the message on Telegram
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.photo, image_recognition))

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
