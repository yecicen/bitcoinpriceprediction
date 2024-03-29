import csv
import math 
import torch
from torch.utils.data import Dataset
import numpy as np
import matplotlib.pyplot as plt    
import datetime

#test from github .

def prepare():
    data = []
    prices = []
    mean_price= 0
    last_date = ""
    counter = 0
    prediction_date = ""
    with open('data/nomics.csv', mode='r') as csv_file:
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
        
        for i in range(3):
            prediction_date = last_date + datetime.timedelta(minutes = (i+1))
            data.append([prediction_date, mean_price])
    with open('nomicsNew.csv', mode='w') as csv_file:
        fieldnames = ['Date', 'Price']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        slicedData = data[-120:]
        for line in slicedData:
            writer.writerow(
            {
                'Date': line[0],
                'Price': line[1]
            })
    print(f"data prepared successfully, last prediction date is {prediction_date}")
prepare()