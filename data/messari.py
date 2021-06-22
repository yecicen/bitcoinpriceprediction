import requests 
import time
from datetime import datetime as dt
import csv
import dateutil.parser
import constants


def run():
    counter = 0
    while True:
        try:
            with open('messari.csv', mode='a') as csv_file:
                fieldnames = ['timestamp', 'price', 'volume']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()
                r = requests.get(url = constants.MESSARI_URL) 
                json_data  = r.json()
                writer.writerow(
                    {
                    'timestamp': int(dateutil.parser.parse(str(json_data['status']['timestamp'])).timestamp()),
                    'price': format(float(json_data['data']['market_data']['price_usd']), ".6f"),
                    'volume': format(float(json_data['data']['market_data']['volume_last_24_hours']), ".6f"),
                    })
                counter = counter + 1
                time.sleep(60.0)
                if counter == constants.DATA_FETCH_LIMIT:
                    break
        except Exception as e:
            print(e)
            time.sleep(60.0)

