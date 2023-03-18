import requests
from pprint import pprint
from operator import itemgetter
url = "https://akabab.github.io/superhero-api/api//all.json"

response = requests.get(url)
data = response.json()
def compare_int(heroes):
    top_int = {}
    for hero in data:
        if hero.get('name') in heroes:
            top_int[hero.get('name')] = hero.get('powerstats').get('intelligence')
    print(max(top_int, key=top_int.get))

compare_int(['Thanos', 'Hulk', 'Captain America'])



