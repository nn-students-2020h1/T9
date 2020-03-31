import csv
import datetime
from io import StringIO

import requests


class CsvTable():
    def __init__(self):
        self.table = []

    def save_table(self, file_name):
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.table[0].keys())
            writer.writeheader()
            for row in self.table:
                writer.writerow(row)

    def load_table(self, file_name):
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            for line in csv.DictReader(csvfile):
                row = {}
                for key in line.keys():
                    row[key] = line[key]
                self.table.append(row)


class CovidTable(CsvTable):
    def get_table(self, date=datetime.datetime.today()):
        while True:
            str_date = date.strftime("%m-%d-%Y")
            url = f"https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{str_date}.csv"
            response = requests.get(url)

            if response.status_code == 200:
                for line in csv.DictReader(StringIO(response.text)):
                    row = {}
                    for key in line.keys():
                        row[key] = line[key]
                    self.table.append(row)
                return str_date
            else:
                date -= datetime.timedelta(days=1)

    def get_confirmed_top(self, location):
        info = [(line[location], int(line["Confirmed"]))
                for line in self.table if line[location] != '']

        info = sorted(info, key=lambda x: int(x[1]))

        top = {x[0]: x[1] for x in info}
        top = sorted(top.items(), key=lambda kv: kv[1], reverse=True)
        return top


if __name__ == "__main__":
    c = CovidTable()
    date = c.get_table()
    # c.save_table("covid.csv")
    # c.load_table("covid.csv")
    info = c.get_confirmed_top("Province_State")
    print(info[:5])
    info = c.get_confirmed_top("Country_Region")
    print(info[:5])
