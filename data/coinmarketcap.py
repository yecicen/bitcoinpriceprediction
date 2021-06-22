from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
import csv
import config
import dateutil.parser
import constants

def run():
  while True:
    try:
      counter = 0
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
      with open('coinmarketcap.csv', mode='a') as csv_file:
          fieldnames = ['timestamp', 'price', 'volume']
          writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

          writer.writeheader()
          response = session.get(constants.COINMARKETCAP_URL, params=parameters)
          json_data = json.loads(response.text)
          print(json_data['data'][0])
          writer.writerow(
              {
          'timestamp': int(dateutil.parser.parse(str(json_data['status']['timestamp'])).timestamp()),
          'price': format(float(json_data['data'][0]['quote']['USD']['price']), ".6f"),
          'volume': format(float(json_data['data'][0]['quote']['USD']['volume_24h']), ".6f"),
          })
          counter = counter + 1
          time.sleep(60.0)
          if counter == constants.DATA_FETCH_LIMIT:
              break
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        time.sleep(60.0)