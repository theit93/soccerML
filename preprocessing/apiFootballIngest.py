import urllib.request
import ssl

import os
print(os.environ['X-Mashape-Key'])

headers = {"X-Mashape-Key": os.environ['X-Mashape-Key'], "Accept": "application/json"}

req = urllib.request.Request(url="https://api-football-v1.p.mashape.com/fixtures/date/2018-12-12", headers=headers)
with urllib.request.urlopen(req, context=ssl._create_unverified_context()) as response:
   body = response.read()
   print(body)