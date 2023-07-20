import requests
from pprint import pprint

url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)
file = (resp.json())
# pprint(file)


hero_names = [ "Hulk", "Captain America", "Thanos"]
intelligence = {}

for character in file:
    if character['name'] in hero_names:
        intelligence[character['powerstats']['intelligence']] = character['name']

sorted_intelligence = dict(sorted(intelligence.items()))
# print(sorted_intelligence)

max_intelligence, smartest_hero = max(intelligence.items(), key=lambda x: x[1])
print(f'Самый умный супергерой: {smartest_hero}\nУровень интеллекта: {str(max_intelligence)}')
