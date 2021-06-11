import csv
import math 
import torch
from torch.utils.data import Dataset
class CustomData(Dataset):
    def __init__(self, source, timestamp, price, volume):
        self.source = source
        self.timestamp = timestamp
        self.volume = volume
        self.price = price
    def len(self):
        return len(self.source)
    def get(self, idx):
        #https://pytorch.org/tutorials/beginner/basics/data_tutorial.html
        return self.source[idx], self.timestamp[idx], self.volume[idx], self.price[idx]

def getDataSet():
    source = []
    timestamp = []
    volume = []
    price = []

    with open('data/messari.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            # special_data = [1,int(row["timestamp"]),float(row["price"]),float(row["volume"]) ]
            source.append(1)
            timestamp.append(int(float(row["timestamp"])))
            price.append(float(row["price"]))
            volume.append(float(row["volume"]))
            line_count += 1
            
    with open('data/nomics.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            # special_data = [2,int(row["timestamp"]),float(row["price"]),float(row["volume"]) ]
            source.append(2)
            timestamp.append(int(float(row["timestamp"])))
            price.append(float(row["price"]))
            volume.append(float(row["volume"]))
            line_count += 1
    with open('data/coinmarketcap.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            # special_data = [3,int(row["timestamp"]),float(row["price"]),float(row["volume"]) ]
            source.append(3)
            timestamp.append(int(float(row["timestamp"])))
            price.append(float(row["price"]))
            volume.append(float(row["volume"]))
            line_count += 1
    
    train_source = source[:(math.ceil(len(source)*0.7))]
    test_source = source[(math.ceil(len(source)*0.7)):]
    train_timestamp = timestamp[:(math.ceil(len(timestamp)*0.7))]
    test_timestamp = timestamp[(math.ceil(len(timestamp)*0.7)):]
    train_price = price[:(math.ceil(len(price)*0.7))]
    test_price = price[(math.ceil(len(price)*0.7)):]
    train_volume = volume[:(math.ceil(len(volume)*0.7))]
    test_volume = volume[(math.ceil(len(volume)*0.7)):]
    train_dataset = CustomData(train_source,train_timestamp,train_price,train_volume)
    test_dataset = CustomData(test_source,test_timestamp,test_price,test_volume)
    return train_dataset, test_dataset
