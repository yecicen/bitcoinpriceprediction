# from bitcoin import Bitcoin
import requests 
import time
from datetime import datetime as dt
import csv
import constants

def run():
    counter = 0
    while True:
        with open('coindesk.csv', mode='a') as csv_file:
            fieldnames = ['timestamp', 'ISOTime', 'price']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()

            r = requests.get(url = constants.COINDESK_URL) 
            json_data  = r.json()
            writer.writerow(
                {'timestamp': json_data['time']['updated'], 
                'ISOTime': json_data['time']['updatedISO'],
                'price': json_data['bpi']['USD']['rate_float']
                })
            counter = counter + 1
            time.sleep(60.0)
            if counter == constants.DATA_FETCH_LIMIT:
                break
