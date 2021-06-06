import requests 
import time
from datetime import datetime as dt
import csv
import config

NOMICS_URL = f'https://api.nomics.com/v1/currencies/ticker?key={config.getApiKey("nomics")}&ids=BTC&interval=1d&convert=USD&per-page=100&page=1'
r = requests.get(url = NOMICS_URL) 
json_data  = r.json()
print(json_data[0]['price_timestamp'])
print(json_data[0]['price'])
counter = 0
with open('nomics.csv', mode='a') as csv_file:
    fieldnames = ['price_timestamp', 'price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    while True:
        r = requests.get(url = NOMICS_URL) 
        json_data  = r.json()
        writer.writerow(
            {
             'price_timestamp': str(json_data[0]['price_timestamp']),
             'price': str(json_data[0]['price'])
            })
        counter = counter + 1
        time.sleep(60.0)
        if counter == 3:
            break
