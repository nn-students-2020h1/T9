import requests
from bs4 import BeautifulSoup


class Weather:
    URL = "https://yandex.ru/pogoda"

    @staticmethod
    def get_data(count_of_days: int = None) -> list:
        soup = BeautifulSoup(requests.get(Weather.URL).text, 'lxml')

        days = list(map(lambda x: x.text, soup.find_all(
            "time", attrs={"class": "time forecast-briefly__date"})))

        week_days = list(map(lambda x: x.text, soup.find_all(
            "div", attrs={"class": "forecast-briefly__name"})))

        temp_day = list(map(lambda x: x.text, soup.find_all(
            "div", attrs={"class": "temp forecast-briefly__temp forecast-briefly__temp_day"})))

        temp_night = list(map(lambda x: x.text, soup.find_all(
            "div", attrs={"class": "temp forecast-briefly__temp forecast-briefly__temp_night"})))

        conditions = list(map(lambda x: x.text, soup.find_all(
            "div", attrs={"class": "forecast-briefly__condition"})))

        _slice = week_days.index('Сегодня')

        return list(zip(
            days[_slice:],
            week_days[_slice:],
            temp_day[_slice:],
            temp_night[_slice:],
            conditions[_slice:]
        ))[:count_of_days]

    @staticmethod
    def get_daylight_info() -> dict:
        soup = BeautifulSoup(requests.get(Weather.URL).text, 'lxml')

        daylight_time = soup.find(
            "div",
            attrs={"class": "sun-card__day-duration-value"},
        ).text

        sunrise_time = soup.find(
            "div",
            attrs={"class": "sun-card__sunrise-sunset-info sun-card__sunrise-sunset-info_value_rise-time"},
        ).text[-5:]

        sunset_time = soup.find(
            "div",
            attrs={"class": "sun-card__sunrise-sunset-info sun-card__sunrise-sunset-info_value_set-time"},
        ).text[-5:]

        day_info = list(map(lambda x: x.text, soup.find_all(
            "div", attrs={"class": "sun-card__text-info-value"})))

        return {
            'daylight_time': daylight_time,
            'sunrise_time': sunrise_time,
            'sunset_time': sunset_time,
            'day_info': day_info,
        }
