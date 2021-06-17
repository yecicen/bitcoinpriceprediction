import time
import data_prep
import lstm
while True:
    lstm.run()
    time.sleep(30.0)
    data_prep.prepare()
    time.sleep(30.0)