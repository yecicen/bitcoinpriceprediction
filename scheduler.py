import time
# import data_prep
import lstm

import data_provider

source ="nomics"
data_provider.preparePredictionData("nomics")
# data_provider.prepareTrendData()
while True:
    lstm.run(source)
    time.sleep(10.0)
    data_provider.preparePredictionData(source)
