import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OMDB_API")

api_params = {
    "url": "http://www.omdbapi.com/",
    "key": api_key,
    "page": "1"
}

def search_movie(title):
    r = requests.get(
    f"{api_params['url']}?apikey={api_params['key']}&t={title}&page={api_params['page']}"
    )

    print(r.json())

    return r.status_code, r.json()