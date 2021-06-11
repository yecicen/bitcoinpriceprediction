import data_provider as dp
# source, timestamp, price, volume = dp.getDataSet()
train, test = dp.getDataSet()
print(test.get(0))