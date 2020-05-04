from functools import reduce
from time import localtime, strftime

from bot.setup import db
from content import utils
from content.CovidInfo import CovidInfo
from content.web_api import get_image_tags


def covid(type: str, count: int) -> str:
    current_date = strftime("%Y-%m-%d", localtime())

    WEBSITE_URL = "https://bitlowsky.github.io/covid-19-info"

    COVID_FUNC = {
        'country_stats': CovidInfo.get_country_top,
        'country_dynamic': CovidInfo.get_country_dynamic_top,
        'province_stats': CovidInfo.get_province_top,
        'province_dynamic': CovidInfo.get_province_dynamic_top,
    }

    COVID_FORMAT = {
        'country_stats': lambda msg, x: msg + f'{x["countryregion"]}: {x["confirmed"]}\n',
        'country_dynamic': lambda msg, country: msg + f'{country["countryregion"]} ({country["lastdynamic"]} | {country["prevdynamic"]})\n',
        'province_stats': lambda msg, province: msg + f'{province["provincestate"]}, {province["countryregion"]}: {province["confirmed"]}\n',
        'province_dynamic': lambda msg, province: msg + f'{province["provincestate"]}, {province["countryregion"]} ({province["lastdynamic"]} | {province["prevdynamic"]})\n',
    }

    COVID_HEADER = {
        'country_stats': "Latest info about the most infected countries:\n",
        'country_dynamic': "Country dynamic top:\n",
        'province_stats': "Latest info about the most infected provinces:\n",
        'province_dynamic': "Province dynamic top:\n",
    }

    data = db.covid.find_one({
        'type': type,
        'date': current_date
    })

    if not data:
        try:
            data = COVID_FUNC[type](count)
            db.covid.insert_one({
                'type': type,
                'data': data,
                'date': current_date
            })
        except Exception:
            pass
    else:
        data = data['data']

    msg = reduce(
        COVID_FORMAT[type],
        data,
        COVID_HEADER[type] if len(data)
        else "Information not found",
    )
    msg += "\nSee more on our website:\n" + WEBSITE_URL

    return msg


def history(user_id):
    logs = utils.get_history(user_id, 5)

    return reduce(
        lambda msg, log: msg + f"{log['call']}:({log['message']})\n",
        logs,
        'Action history:\n' if len(logs)
        else "Information not found",
    )


def image_recognition(image_url):
    tags = get_image_tags(image_url)

    return reduce(
        lambda msg, tag: msg + '\n*' + tag,
        tags,
        'On the picture:' if len(tags)
        else "Information not found",
    )
