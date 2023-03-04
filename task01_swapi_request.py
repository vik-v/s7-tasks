from typing import Dict
import requests
from pprint import pprint

BASE_URL = 'https://swapi.dev/api/'
RESOURCE = 'people/'
SEARCH_URL = '?search='
REQUEST_LIMIT = 10


def query(resource: str, *args,
          url: str = BASE_URL) -> Dict[str, str]:
    return requests.get(url + resource + ''.join(args)).json()


response = query(RESOURCE, '?search=Luke').get('results')[:REQUEST_LIMIT]
planet = requests.get(response[0].get('homeworld')).json()
diameter = planet.get('diameter')

pprint(int(diameter))
