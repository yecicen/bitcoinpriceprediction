from bitcoin import Bitcoin
import requests 
import time
from datetime import datetime as dt


COINDESK_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

bitcoins = []

while True:
    r = requests.get(url = COINDESK_URL) 
    json_data  = r.json()
    btc = Bitcoin(0,0)
    btc.date = json_data['time']['updated']
    btc.price = json_data['bpi']['USD']['rate_float']
    bitcoins.append(btc)
    time.sleep(30.0)
    if len(bitcoins) == 2:
        break

for btc in bitcoins:
    print(btc.price)
