import time
import data_provider
import lstm_trend

source ="nomics"
data_provider.prepareTrendData(source)
while True:
    lstm_trend.run(source)
    time.sleep(10.0)
    data_provider.prepareTrendData(source)

