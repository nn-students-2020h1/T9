import requests


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
