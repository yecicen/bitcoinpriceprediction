from time import time
import numpy as np
import pandas as pd
from pylab import plt
import math
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import torch
import torch.nn as nn
import requests
import datetime
import data.config as config
import csv


def load_data(btc_data, look_back):
    data_raw = btc_data.values
    data = []

    # create all possible sequences of length
    for index in range(len(data_raw) - look_back):
        data.append(data_raw[index: index + look_back])

    data = np.array(data)
    test_set_size = int(np.round(0.2*data.shape[0]))
    train_set_size = data.shape[0] - (test_set_size)

    x_train = data[:train_set_size, :-1, :]
    y_train = data[:train_set_size, -1, :]

    x_test = data[train_set_size:, :-1]
    y_test = data[train_set_size:, -1, :]

    return [x_train, y_train, x_test, y_test]


# model
input_dim = 2
hidden_dim = 50
num_layers = 2
output_dim = 2


# model class
class LSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers, output_dim):
        super(LSTM, self).__init__()

        self.hidden_dim = hidden_dim

        # Number of hidden layers
        self.num_layers = num_layers

        self.lstm = nn.LSTM(input_dim, hidden_dim,
                            num_layers, batch_first=True)

        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        # Initialize hidden state
        h0 = torch.zeros(self.num_layers, x.size(
            0), self.hidden_dim).requires_grad_()

        # Initialize cell state
        c0 = torch.zeros(self.num_layers, x.size(
            0), self.hidden_dim).requires_grad_()

        # detach backpropagation
        out, (hn, cn) = self.lstm(x, (h0.detach(), c0.detach()))

        # step the hidden states
        out = self.fc(out[:, -1, :])
        return out


def run():
    df_btc = pd.read_csv("updown.csv", parse_dates=True, index_col=0)
    last_date = df_btc.index[-1]
    earlier_date = df_btc.index[-2]
    scaler = MinMaxScaler(feature_range=(-1, 1))
    # df_btc['Trend'] = scaler.fit_transform(df_btc['Price'].values.reshape(-1,1))

    look_back = 30
    x_train, y_train, x_test, y_test = load_data(df_btc, look_back)

    x_train = torch.from_numpy(x_train).type(torch.Tensor)
    x_test = torch.from_numpy(x_test).type(torch.Tensor)
    y_train = torch.from_numpy(y_train).type(torch.Tensor)
    y_test = torch.from_numpy(y_test).type(torch.Tensor)

    model = LSTM(input_dim=input_dim, hidden_dim=hidden_dim,
                 output_dim=output_dim, num_layers=num_layers)

    loss_fn = torch.nn.MSELoss()

    optimiser = torch.optim.Adam(model.parameters(), lr=0.01)

    # Train model
    num_epochs = 200
    hist = np.zeros(num_epochs)

    # Number of steps to unroll
    seq_dim = look_back-1

    for t in range(num_epochs):
        # Forward pass
        y_train_pred = model(x_train)

        loss = loss_fn(y_train_pred, y_train)
        if t % 10 == 0 and t != 0:
            print("Epoch ", t, "MSE: ", loss.item())
        hist[t] = loss.item()

        # detach gradients
        optimiser.zero_grad()

        # Backward pass
        loss.backward()

        # Update parameters
        optimiser.step()

    # make predictions
    y_test_pred = model(x_test)

    # invert predictions
    y_train_pred = y_train_pred.detach().numpy()
    y_train = y_train.detach().numpy()
    y_test_pred = y_test_pred.detach().numpy()
    y_test = y_test.detach().numpy()

    # calculate root mean squared error
    trainScore = math.sqrt(mean_squared_error(
        y_train[:, 0], y_train_pred[:, 0]))
    print('Train Score: %.2f RMSE' % (trainScore))
    testScore = math.sqrt(mean_squared_error(y_test[:, 0], y_test_pred[:, 0]))
    print('Test Score: %.2f RMSE' % (testScore))

    # Visualising the results
    # figure, axes = plt.subplots(figsize=(15, 6))
    # axes.xaxis_date()

    # axes.plot(df_btc[len(df_btc)-len(y_test):].index, y_test, color = 'green', label = 'Real BTC Price')
    # axes.plot(df_btc[len(df_btc)-len(y_test):].index, y_test_pred, color = 'blue', label = 'Predicted BTC Price')

    # post this data to website
    predicted_trend, predicted_rate = y_test_pred[-1]
    print(y_test_pred[-1])
    trend = "Up"
    if(predicted_trend < 0.5):
        trend = "Down"
    # when time is 5 minutes, get actual price, and send the prediction to api
    counter = 0
    predictDate = last_date.strftime("%Y-%m-%d %H:%M:%S")
    earlier_predictDate = earlier_date.strftime("%Y-%m-%d %H:%M:%S")
    earlier_actual_price = 0
    actual_price = 0
    api_url = f'https://api.nomics.com/v1/currencies/ticker?key={config.getApiKey("nomics")}&ids=BTC&interval=1d&convert=USD&per-page=100&page=1'
    print(
        f"earlier_predictDate: {earlier_predictDate} predictDate: {predictDate} predicted_rate: {predicted_rate}")
    while True:
        dateString = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if earlier_predictDate < dateString:
            print(f"dateString {dateString}")
            if counter == 0:
                counter = counter + 1
                try:
                    r = requests.get(url=api_url)
                    json_data = r.json()
                    earlier_actual_price = float(
                        format(float(json_data[0]['price']), ".6f"))
                    print(f"earlier_actual_price {earlier_actual_price}")
                    while True:
                        dateString = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        if predictDate < dateString:
                            if counter == 1:
                                counter = counter + 1
                                try:
                                    r = requests.get(url=api_url)
                                    json_data = r.json()
                                    actual_price = float(
                                        format(float(json_data[0]['price']), ".6f"))
                                    print(f"actual_price {actual_price}")
                                    actual_rate = (
                                        float(actual_price) - float(earlier_actual_price)) / float(actual_price)
                                    actual_trend = "Up"
                                    if(actual_rate < 0):
                                        actual_trend = "Down"
                                    with open('trendOutput.csv', mode='a') as csv_file:
                                        fieldnames = [
                                            'date', 'predicted_trend', 'actual_trend', 'predicted_rate', 'actual_rate']
                                        writer = csv.DictWriter(
                                            csv_file, fieldnames=fieldnames)
                                        writer.writerow(
                                            {
                                                'date': dateString,
                                                'predicted_trend': trend,
                                                'actual_trend': actual_trend,
                                                'predicted_rate': abs(float(format(float(predicted_rate), ".6f"))),
                                                'actual_rate': abs(float(format(float(actual_rate), ".6f")))
                                            }
                                        )
                                        print("inside while ending")
                                        break
                                except Exception as e: 
                                    print(e)
                                    break
                    print("outside while ending")
                    break
                except Exception as e: 
                    print(e)
                    break

    # plt.title('BTC Price Prediction')
    # plt.xlabel('Time')
    # plt.ylabel('BTC Price')
    # plt.legend()
    # plt.savefig('BTC_pred.png')
    # plt.show()
# run()
