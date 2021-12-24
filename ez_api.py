import requests


url = "https://politicsandwar.com/api/"


def req(link, key, connector="&key="):
    return requests.get(f"{url}{link}{connector}{key}").json()
