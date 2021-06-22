import csv
import math 
import torch
from torch.utils.data import Dataset
import numpy as np
import matplotlib.pyplot as plt    
import datetime

def preparePredictionData(data_source):
    data = []
    prices = []
    mean_price= 0
    last_date = ""
    prediction_date = ""
    provider_path = "data/" + data_source +".csv"
    output_path = data_source + ".csv"
    with open(provider_path, mode='r') as csv_file:
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
    with open(output_path, mode='w') as csv_file:
        fieldnames = ['Date', 'Price']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        slicedData = data[-480:]
        for line in slicedData:
            writer.writerow(
            {
                'Date': line[0],
                'Price': line[1]
            })
    print(f"data prepared successfully, last prediction date is {prediction_date}")

def prepareTrendData(data_source):
    data = []
    prices = []
    last_date = ""
    prediction_date = ""
    provider_path = "data/" + data_source +".csv"
    output_path = data_source +"_Trend"+ ".csv"
    with open(provider_path, mode='r') as csv_file:
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
        
        for i in range(3):
            prediction_date = last_date + datetime.timedelta(minutes = (i+1))
            data.append([prediction_date, prices[-1:][0]])
    with open(output_path, mode='w') as csv_file:
        fieldnames = ['Date', 'Trend', 'Rate']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        slicedData = data[-120:]
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

preparePredictionData("nomics")