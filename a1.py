import requests
import json

# Example prints: miejsce gdzie znajduje sie stacja kosmiczna :)))
site = "http://api.open-notify.org/iss-now.json"
res = requests.get(site)  # get data from API

d = json.loads(res.text)
print(d['timestamp'])
print(d['iss_position']['longitude'], d['iss_position']['latitude'])
