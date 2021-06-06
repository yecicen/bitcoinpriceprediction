import requests 
import time
from datetime import datetime as dt
import csv

URL = "https://data.messari.io/api/v1/assets/btc/metrics"

counter = 0
with open('messari.csv', mode='a') as csv_file:
    fieldnames = ['price_timestamp', 'price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    while True:
        r = requests.get(url = URL) 
        json_data  = r.json()
        writer.writerow(
            {
             'price_timestamp': str(json_data['status']['timestamp']),
             'price': str(json_data['data']['market_data']['price_usd']),
            })
        counter = counter + 1
        time.sleep(60.0)
        if counter == 3:
            break

