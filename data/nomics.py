import requests 
import time
from datetime import datetime as dt
import csv
import config
import dateutil.parser

NOMICS_URL = f'https://api.nomics.com/v1/currencies/ticker?key={config.getApiKey("nomics")}&ids=BTC&interval=1d&convert=USD&per-page=100&page=1'
counter = 0
limit = 240
with open('nomics.csv', mode='a') as csv_file:
    fieldnames = ['timestamp', 'price', 'volume']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    while True:
        r = requests.get(url = NOMICS_URL) 
        json_data  = r.json()
        writer.writerow(
            {
             'timestamp': int(dateutil.parser.parse(str(json_data[0]['price_timestamp'])).timestamp()),
             'price': format(float(json_data[0]['price']), ".6f"),
             'volume': format(float(json_data[0]['1d']['volume']), ".6f"),
            })
        counter = counter + 1
        time.sleep(60.0)
        if counter == limit:
            break
