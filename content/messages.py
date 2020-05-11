from functools import reduce
from time import localtime, strftime, time

from bot.setup import db
from content import utils
from content.CovidInfo import CovidInfo
from content.web_api import get_image_tags
from content.utils import format_date


def covid(type: str, count: int, date=None) -> str:
    '''!!!date parameter only works with country_stats type!!!'''

    WEBSITE_URL = "https://bitlowsky.github.io/covid-19-info"

    COVID_FUNC = {
        'country_stats': CovidInfo.get_country_top if not date else CovidInfo.get_country_top_by_date,
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

    yesterday = strftime("%d/%m/%y", localtime(time() - 3600 * 24))
    date = format_date(yesterday if not date else date)

    COVID_HEADER = {
        'country_stats': f"Country stats top on {date}:\n",
        'country_dynamic': f"Country dynamic top on {date}:\n",
        'province_stats': f"Province stats top on {date}:\n",
        'province_dynamic': f"Province dynamic top on {date}:\n",
    }

    data = db.covid.find_one({
        'type': type,
        'date': date
    })

    if not data:
        try:
            data = COVID_FUNC[type](count)

        except Exception:
            data = COVID_FUNC[type](date, count)

        finally:
            if len(data):
                db.covid.insert_one({
                    'type': type,
                    'data': data,
                    'date': date
                })

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
