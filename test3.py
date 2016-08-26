
import requests
import pprint

url = 'http://www.google.co.uk'
r = requests.get(url)

print r.status_code, 'thisi '
pprint.pprint(r.headers)
