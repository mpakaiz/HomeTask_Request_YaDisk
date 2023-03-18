import requests

from pprint import pprint
url = "https://api.stackexchange.com/2.3/questions?fromdate=1678924800&todate=1679097600&order=desc&sort=activity&tagged=python&site=stackoverflow"

response = requests.get(url)
data = response.json()
pprint(data)