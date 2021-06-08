from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
import csv
import config

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'1',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.getApiKey("coinmarketcap"),
}

session = Session()
session.headers.update(headers)

try:
    counter = 0
    limit = 240
    with open('coinmarketcap.csv', mode='a') as csv_file:
        fieldnames = ['timestamp', 'price', 'volume']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        while True:
            response = session.get(url, params=parameters)
            json_data = json.loads(response.text)
            print(json_data['data'][0])
            writer.writerow(
                {
                'timestamp': str(json_data['status']['timestamp']),
                'price': str(json_data['data'][0]['quote']['USD']['price']),
                'volume': str(json_data['data'][0]['quote']['USD']['volume_24h'])
                })
            counter = counter + 1
            time.sleep(60.0)
            if counter == limit:
                break
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)