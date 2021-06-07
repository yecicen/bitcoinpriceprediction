import requests 
import time
from datetime import datetime as dt
import csv

URL = "https://data.messari.io/api/v1/assets/btc/metrics"

counter = 0
with open('messari.csv', mode='a') as csv_file:
    fieldnames = ['timestamp', 'price', 'volume']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    while True:
        r = requests.get(url = URL) 
        json_data  = r.json()
        writer.writerow(
            {
             'timestamp': str(json_data['status']['timestamp']),
             'price': str(json_data['data']['market_data']['price_usd']),
             'volume': str(json_data['data']['market_data']['volume_last_24_hours']),
            })
        counter = counter + 1
        time.sleep(60.0)
        if counter == 3:
            break

