import csv
import datetime

import requests
from bs4 import BeautifulSoup


def get_quote():
    html = requests.get("https://icitaty.ru/random/").text
    soup = BeautifulSoup(html, "lxml")

    text = soup.find("p").text
    author = soup.find("a", attrs={"title": "Автор цитаты"})
    book = soup.find("a", attrs={"title": "Цитаты из книги"})
    person = soup.find("a", attrs={"title": "Цитируемый персонаж"})

    author = str(author)[str(author).find("</i>") + 4:str(author).find("</a>")]
    book = str(book)[str(book).find("</i>") + 4:str(book).find("</a>")]
    person = str(person)[str(person).find("</i>") + 4:str(person).find("</a>")]

    author = ' '.join(author.split())
    book = ' '.join(book.split())
    person = ' '.join(person.split())

    return text, author, book, person


class Cat:
    @staticmethod
    def get_fact():
        response = requests.get('https://cat-fact.herokuapp.com/facts/random')
        data = response.json()
        return data['text']

    @staticmethod
    def get_image():
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        imgData = response.json()
        return imgData[0]["url"]


class CoronaStats:
    @staticmethod
    def collect_stats(location):
        actual = CoronaStats._actual_update()
        infected = CoronaStats._read_table(location)
        stats = \
            f'The most infected {location.lower().split("_")[0].replace("y", "ie") + "s"} on {actual.strftime("%d.%m.%Y")}:\n'
        for key, value in infected.items():
            stats += (key + ': ' + value + '\n')
        return stats

    @staticmethod
    def _actual_update():
        actual = datetime.datetime.today()
        r = CoronaStats._get_table(actual.strftime("%m-%d-%Y"))
        delta = datetime.timedelta(days=1)
        while r.status_code != 200:
            actual = actual - delta
            r = CoronaStats._get_table(actual.strftime("%m-%d-%Y"))
        CoronaStats._download_table(r)
        return actual

    @staticmethod
    def _get_table(data):
        return requests.get(
            f"https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{data}.csv")

    @staticmethod
    def _download_table(r):
        with open('virus.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csvfile.writelines(r.text)

    @staticmethod
    def _read_table(location):
        infected = {}
        with open('virus.csv', 'r') as csvfile:
            sortedlist = sorted(csv.DictReader(csvfile), key=lambda row: int(
                row['Confirmed']), reverse=True)
            for row in sortedlist:
                if row[location] == '':
                    continue
                infected.update({row[location]: row['Confirmed']})
                if len(infected) == 5:
                    break
        return infected
