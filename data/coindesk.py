# from bitcoin import Bitcoin
import requests 
import time
from datetime import datetime as dt
import csv

COINDESK_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
counter = 0
with open('coindesk.csv', mode='a') as csv_file:
    fieldnames = ['time', 'ISOTime', 'price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    while True:
        r = requests.get(url = COINDESK_URL) 
        json_data  = r.json()
        writer.writerow(
            {'time': json_data['time']['updated'], 
             'ISOTime': json_data['time']['updatedISO'],
             'price': json_data['bpi']['USD']['rate_float']
            })
        counter = counter + 1
        time.sleep(60.0)
        if counter == 1800:
            break
