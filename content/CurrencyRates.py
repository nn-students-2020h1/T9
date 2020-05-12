import requests
from bs4 import BeautifulSoup


class CurrencyRates:
    URL = 'https://cbr.ru/key-indicators/'

    @staticmethod
    def get_currency_rates():
        soup = BeautifulSoup(requests.get(CurrencyRates.URL).text, 'lxml')

        names = list(map(
            lambda x: x.find("div", attrs={"class": "col-md-3 offset-md-1 _subinfo"}).text,
            soup.find_all("div", attrs={"class": "d-flex title-subinfo"}),
        ))

        current_rates = list(map(lambda x: x.text, soup.find_all(
            "td", attrs={"class": "value td-w-4 _bold _end mono-num _with-icon _down _green"})))

        metal_rates = list(map(lambda x: x.text, soup.find_all(
            "td", attrs={"class": "value td-w-4 _bold _end mono-num"})))

        rates = current_rates + metal_rates[2:]

        return list(zip(names, map(lambda rate: rate + ' RUB', rates)))
