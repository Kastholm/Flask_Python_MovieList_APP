import requests
import datetime

date = datetime.datetime.now()

api_params = {
    "url": "http://www.omdbapi.com/",
    "key": "1234",
    "page": "1"
}

def get_movie(title):
    r = requests.get(
    f"{api_params['url']}?apikey={api_params['key']}&t={title}&page={api_params['page']}"
    )

    return r.status_code, r.json()


def save_movie(status):

    if status == 200:
        print('movie added')