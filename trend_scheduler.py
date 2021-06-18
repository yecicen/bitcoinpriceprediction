import time
import data_updown
import lstm_trend
while True:
    print("running lstm model")
    lstm_trend.run()
    print("finishing lstm model")
    time.sleep(30.0)
    print("preparing data again")
    data_updown.prepare()
