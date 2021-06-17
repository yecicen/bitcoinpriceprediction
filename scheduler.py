import time
import kg_data
import lstm
while True:
    lstm.run()
    time.sleep(30.0)
    kg_data.prepare()
    time.sleep(30.0)