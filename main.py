# -*- coding: utf-8 -*-
from threading import Thread

import requests
from telegram import Bot
from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater)

from bot.handlers import (
    cat_fact, cat_image, chat_help, content_menu, country_dynamic,
    country_stats, covid_menu, currency_rates, echo, error, history,
    image_recognition, main_menu, meme, province_dynamic, province_stats,
    start, weather, wiki)
from bot.log import logger
from bot.setup import PROXY, TOKEN


def main():
    bot = Bot(token=TOKEN, base_url=PROXY)
    updater = Updater(bot=bot, use_context=True)
    Thread(target=requests.get, kwargs={'url': 'https://bitlowsky-api.herokuapp.com/init/'}).start()

    # on different commands - answer in Telegram
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', chat_help))
    updater.dispatcher.add_handler(CommandHandler('history', history))

    updater.dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('weather', weather)],
        states={
            1: [MessageHandler(Filters.regex(r'\d+|all'), weather)],
        },
        fallbacks=[CommandHandler('main', main_menu)]
    ))

    updater.dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('country_stats', country_stats)],
        states={
            1: [MessageHandler(Filters.regex(
                r'^(/latest|(0?[1-9]|[12][0-9]|3[01])[\- ./](0?[1-9]|1[012])[\- ./](20[0-9]{2}|[0-9]{4}|[0-9]{2}))$'),
                country_stats)],
        },
        fallbacks=[CommandHandler('main', main_menu)]
    ))

    updater.dispatcher.add_handler(ConversationHandler(
        entry_points=[MessageHandler(Filters.photo, image_recognition)],
        states={
            1: [MessageHandler(Filters.regex(r'tags|wiki'), image_recognition)],
        },
        fallbacks=[CommandHandler('main', main_menu)]
    ))

    updater.dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('wiki', wiki)],
        states={
            1: [MessageHandler(Filters.text, wiki)],
        },
        fallbacks=[CommandHandler('main', main_menu)]
    ))

    updater.dispatcher.add_handler(CommandHandler('main', main_menu))
    updater.dispatcher.add_handler(CommandHandler('covid', covid_menu))
    updater.dispatcher.add_handler(CommandHandler('content', content_menu))

    updater.dispatcher.add_handler(CommandHandler('cat_image', cat_image))
    updater.dispatcher.add_handler(CommandHandler('cat_fact', cat_fact))
    updater.dispatcher.add_handler(CommandHandler('meme', meme))
    updater.dispatcher.add_handler(CommandHandler('currency', currency_rates))

    updater.dispatcher.add_handler(CommandHandler('country_dynamic', country_dynamic))
    updater.dispatcher.add_handler(CommandHandler('province_stats', province_stats))
    updater.dispatcher.add_handler(CommandHandler('province_dynamic', province_dynamic))

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
