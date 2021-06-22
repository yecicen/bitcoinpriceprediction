import config

BITMEX_WEBSOCKET_URL = "wss://www.bitmex.com/realtime?subscribe=orderBook10:XBTUSD"
BITMEX_SUB_TOPIC = "orderBook10:XBTUSD"
NOMICS_URL = f'https://api.nomics.com/v1/currencies/ticker?key={config.getApiKey("nomics")}&ids=BTC&interval=1d&convert=USD&per-page=100&page=1'
MESSARI_URL = "https://data.messari.io/api/v1/assets/btc/metrics"
COINMARKETCAP_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
COINDESK_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

DATA_FETCH_LIMIT = 240
DATA_SOURCES = [
    "bitmex"
    ,"coindesk"
    ,"coinmarketcap"
    ,"messari"
    ,"nomics"
    ]