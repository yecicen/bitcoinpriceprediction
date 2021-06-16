import csv
import math 
import torch
from torch.utils.data import Dataset
import numpy as np
import matplotlib.pyplot as plt    
import datetime

data = []
prices = []
mean_price= 0
last_date = ""
with open('test.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        special_data = [datetime.datetime.fromtimestamp(int(row["timestamp"])),float(row["price"]) ]
        last_date = datetime.datetime.fromtimestamp(int(row["timestamp"]))
        prices.append(float(row["price"]))
        data.append(special_data)
        line_count += 1
    mean_price = format(np.mean(np.asarray(prices)), ".6f")
    
    for i in range(5):
        prediction_date = last_date + datetime.timedelta(minutes = (i+1))
        data.append([prediction_date, mean_price])
with open('kgdata.csv', mode='a') as csv_file:
    fieldnames = ['Date', 'Price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for line in data:
        writer.writerow(
        {
            'Date': line[0],
            'Price': line[1]
        })