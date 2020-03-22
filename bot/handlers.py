# -*- coding: utf-8 -*-
import csv
import requests
import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from bot.Buttons2 import reply_keyboard
from bot.log import dataBase, log, logger
from modules import content

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
    /corono_stats - список 5 провинций, где больше всего новых заражённых
    /country_stats - список 5 стран, где больше всего новых заражённых'''

    update.message.reply_text(msg)

def requestGit():
    today = datetime.datetime.today()
    data = today.strftime("%m-%d-%Y")
    r = requests.get(f"https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{data}.csv")
    actual = today
    while r.status_code != 200:
        delta = datetime.timedelta(days=1)
        today = today - delta
        data = today.strftime("%m-%d-%Y")
        r = requests.get(
            f"https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{data}.csv")
        actual = today

    with open('virus.csv', 'w', newline='') as csvfile:
        csvfile.writelines(r.text)
    return actual

@log
def corono_stats(update: Update, context: CallbackContext):
    actual = requestGit()
    infected = {}
    with open('virus.csv', 'r') as file:
        reader = csv.DictReader(file)
        k=0
        for row in reader:
            province = row['Province/State']
            if province == '':
                continue
            confirmed = row["Confirmed"]
            infected.update({province:confirmed})
            k+=1
            if (k==5):
                break

    msg=f'The most infected provinces on {actual.strftime("%d.%m.%Y")}:\n'
    for key, value in infected.items():
        msg+=(key+': '+ value+'\n')
    update.message.reply_text(msg)

@log
def stats_country(update: Update, context: CallbackContext):
    actual = requestGit()
    infected = {}
    with open('virus.csv', 'r') as file:
        reader = csv.DictReader(file)
        k=0
        for row in reader:
            country = row['Country/Region']
            confirmed = row["Confirmed"]
            infected.update({country:confirmed})
            k+=1
            if (k==5):
                break

    msg=f'The most infected countries on {actual.strftime("%d.%m.%Y")}:\n'
    for key, value in infected.items():
        msg+=(key+': '+ value+'\n')
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
def sendQuote(update: Update, context: CallbackContext):
    """Send a message when the command /quote is issued."""
    text, author, book, person = content.getQuote()
    msg = text + '\n'

    if author:
        msg += f"\nАвтор: {author}"
    if book:
        msg += f"\nКнига: {book}"
    if person:
        msg += f"\nПерсонаж: {person}"

    update.message.reply_text(msg)

@log
def sendCatImage(update: Update, context: CallbackContext):
    """Send a photo when the command /cat is issued."""
    update.message.reply_photo(content.getCatImage())

@log
def sendCatFact(update: Update, context: CallbackContext):
    """Send a text when the command /fact is issued."""
    update.message.reply_text(content.getCatFact())

@log
def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')
