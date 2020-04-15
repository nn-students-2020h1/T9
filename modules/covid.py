import requests


class CovidInfo:
    ENDPOINT_URL = "https://wuhan-coronavirus-api.laeyoung.endpoint.ainize.ai/jhu-edu/"
    BRIEF_URL = ENDPOINT_URL + "brief"
    LATEST_URL = ENDPOINT_URL + "latest"
    TIMESERIES_URL = ENDPOINT_URL + "timeseries"

    @staticmethod
    def get_country_top():
        data = CovidInfo.__get_data(
            CovidInfo.LATEST_URL + "?onlyCountries=true")
        return sorted(data, key=lambda country: country["confirmed"], reverse=True)

    @staticmethod
    def get_province_top():
        res = []
        data = CovidInfo.__get_data(CovidInfo.LATEST_URL)

        for x in data:
            if ("confirmed" in x) and (len(x['provincestate']) > 0):
                res.append(x)

        return sorted(res, key=lambda province: province["confirmed"], reverse=True)

    @staticmethod
    def get_country_dynamic_top(count):
        res = []
        data = CovidInfo.get_dynamic_top()

        for x in data:
            if (len(x["provincestate"]) == 0) and (len(res) < count):
                res.append({
                    "countryregion": x["countryregion"],
                    "lastdynamic": x["lastdynamic"],
                    "prevdynamic": x["prevdynamic"],
                })
        return res

    @staticmethod
    def get_province_dynamic_top(count):
        res = []
        data = CovidInfo.get_dynamic_top()

        for x in data:
            if (len(x["provincestate"]) != 0) and (len(res) < count):
                res.append({
                    "provincestate": x["provincestate"],
                    "countryregion": x["countryregion"],
                    "lastdynamic": x["lastdynamic"],
                    "prevdynamic": x["prevdynamic"],
                })
        return res

    @staticmethod
    def get_timeseries():
        data = CovidInfo.__get_data(CovidInfo.TIMESERIES_URL)
        return data

    @staticmethod
    def get_dynamic_top():
        res = []
        data = CovidInfo.get_timeseries()

        dates = list(data[0]["timeseries"].keys())

        for x in data:
            if ("confirmed" in x["timeseries"][dates[len(dates) - 1]]):
                res.append({
                    "provincestate": x["provincestate"],
                    "countryregion": x["countryregion"],
                    "lastdynamic": x["timeseries"][dates[len(dates) - 1]]["confirmed"] - x["timeseries"][dates[len(dates) - 2]]["confirmed"],
                    "prevdynamic": x["timeseries"][dates[len(dates) - 2]]["confirmed"] - x["timeseries"][dates[len(dates) - 3]]["confirmed"],
                })
        return sorted(res, key=lambda x: x["lastdynamic"], reverse=True)

    @staticmethod
    def __get_data(URL):
        response = requests.get(URL)
        return response.json()


if __name__ == "__main__":
    data = CovidInfo.get_country_top()
    print(data)
