import requests


class CovidInfo:
    ENDPOINT_URL = "https://wuhan-coronavirus-api.laeyoung.endpoint.ainize.ai/jhu-edu/"
    BRIEF_URL = ENDPOINT_URL + "brief"
    LATEST_URL = ENDPOINT_URL + "latest"
    TIMESERIES_URL = ENDPOINT_URL + "timeseries"

    @staticmethod
    def get_country_top(count: int) -> list:
        return sorted(
            CovidInfo.get_data(CovidInfo.LATEST_URL + "?onlyCountries=true"),
            key=lambda country: country["confirmed"],
            reverse=True,
        )[:count]

    @staticmethod
    def get_province_top(count: int) -> list:
        return sorted(
            list(filter(
                lambda x: "confirmed" in x and len(x['provincestate']) > 0,
                CovidInfo.get_data(CovidInfo.LATEST_URL),
            )),
            key=lambda province: province["confirmed"],
            reverse=True,
        )[:count]

    @staticmethod
    def get_country_dynamic_top(count: int) -> list:
        return list(map(
            lambda x: {
                    "countryregion": x["countryregion"],
                    "lastdynamic": x["lastdynamic"],
                    "prevdynamic": x["prevdynamic"],
                    },
            list(filter(
                lambda x: len(x["provincestate"]) == 0,
                 CovidInfo.get_dynamic_top()
                 )),
        ))[:count]

    @staticmethod
    def get_province_dynamic_top(count: int) -> list:
        return list(map(
            lambda x: {
                    "provincestate": x["provincestate"],
                    "countryregion": x["countryregion"],
                    "lastdynamic": x["lastdynamic"],
                    "prevdynamic": x["prevdynamic"],
                    },
            list(filter(
                lambda x: len(x["provincestate"]) != 0,
                 CovidInfo.get_dynamic_top()
                 )),
        ))[:count]

    @staticmethod
    def get_dynamic_top() -> list:
        data = CovidInfo.get_data(CovidInfo.TIMESERIES_URL)
        dates = list(data[0]["timeseries"].keys())

        return sorted(list(map(
            lambda x: {
                "provincestate": x["provincestate"],
                "countryregion": x["countryregion"],
                "lastdynamic": x["timeseries"][dates[len(dates) - 1]]["confirmed"] - x["timeseries"][dates[len(dates) - 2]]["confirmed"],
                "prevdynamic": x["timeseries"][dates[len(dates) - 2]]["confirmed"] - x["timeseries"][dates[len(dates) - 3]]["confirmed"],
            },
            list(filter(
                lambda x: "confirmed" in x["timeseries"][dates[len(dates) - 1]],
                data,
            )))),
            key=lambda x: x["lastdynamic"],
            reverse=True,
        )

    @staticmethod
    def get_country_top_by_date(date: str, count: int) -> list:
        data = CovidInfo.get_data(CovidInfo.TIMESERIES_URL + "?onlyCountries=true")
        dates = list(data[0]["timeseries"].keys())

        if date not in dates:
            return []

        countries = []
        for country in data:
            countries.append({
                "countryregion": country["countryregion"],
                "confirmed": country["timeseries"][date]["confirmed"],
                "deaths": country["timeseries"][date]["deaths"],
                "recovered": country["timeseries"][date]["recovered"],
            })

        return sorted(countries, key=lambda country: country["confirmed"], reverse=True)[:count]

    @staticmethod
    def get_timeseries() -> list:
        return CovidInfo.get_data(CovidInfo.TIMESERIES_URL)

    @staticmethod
    def get_data(url):
        try:
            response = requests.get(url)

            if response.ok:
                try:
                    return response.json()

                except Exception:
                    return response.text

            else:
                return None

        except Exception:
            return None
