import csv
import math 
import torch
from torch.utils.data import Dataset
import numpy as np
import matplotlib.pyplot as plt    
import datetime

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
        
        for i in range(4):
            prediction_date = last_date + datetime.timedelta(minutes = (i+1))
            data.append([prediction_date, prices[-1:][0]])
    with open('updown.csv', mode='w') as csv_file:
        fieldnames = ['Date', 'Trend', 'Rate']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        slicedData = data[-244:]
        print(slicedData[0][1])
        for i in range(len(slicedData)-1):
            trend = 0
            price = slicedData[i][1]
            next_price = slicedData[(i+1)][1]
            rate = (float(next_price) - float(price)) / (float(next_price))
            print(f"price {price} next_price {next_price} rate {rate}")
            if(price < next_price):
                trend = 1
            writer.writerow(
            {
                'Date': slicedData[i][0],
                'Trend': trend,
                "Rate": rate
            })
    print(f"data prepared successfully, last prediction date is {prediction_date}")
prepare()