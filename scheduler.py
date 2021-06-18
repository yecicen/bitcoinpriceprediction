import time
import data_prep
import lstm
while True:
    lstm.run()
    time.sleep(10.0)
    data_prep.prepare()
