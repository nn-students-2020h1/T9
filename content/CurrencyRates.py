import requests
from bs4 import BeautifulSoup


class CurrencyRates:
    URL = 'https://cbr.ru/key-indicators/'

    @staticmethod
    def get_currency_rates():
        soup = BeautifulSoup(requests.get(CurrencyRates.URL).text, 'lxml')
        tables = soup.find_all("div", attrs={"class": "table key-indicator_table"})

        tds = []
        for table in tables:
            trs = table.find_all('tr')

            for tr in trs:
                tds.append(list(map(lambda x: x.text, tr.find_all('td'))))

        search = ['USD', 'EUR', 'Au', 'Ag', 'Pt', 'Pd']
        out = []

        for td in tds:
            for x in search:
                if td[0].find(x) != -1:
                    out.append((x, float(td[-1:][0].replace(',', '.').replace(' ', ''))))

        return out


if __name__ == "__main__":
    print(CurrencyRates.get_currency_rates())
