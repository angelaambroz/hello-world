
import requests
import pprint
import json

query_params = { 'apikey': 'f6ab5f2e4f69444b9f2c0a44d9a5223d',
		   		 'phrase': 'equal pay',
		   		 'sort': 'date desc'
		 		}

endpoint = 'http://capitolwords.org/api/text.json'

r = requests.get(endpoint, params=query_params)
data = r.json()
pprint.pprint(data)

with open('equalpay.json', 'w') as outfile:
     json.dump(data, outfile, sort_keys = True, indent = 4,
ensure_ascii=False)
