# import data_provider as dp
# import datetime
# source, timestamp, price, volume = dp.getDataSet()
# train, test = dp.getDataSet()
# print(test.get(0))

# print(datetime.datetime.now().strftime("%m-%d-%Y, %H:%M:%S"))
from datetime import datetime
myFile = open('append.txt', 'a') 
myFile.write('\nAccessed on ' + str(datetime.now()))