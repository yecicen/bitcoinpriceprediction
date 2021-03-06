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

NOMICS_URL = f'https://api.nomics.com/v1/currencies/ticker?key={config.getApiKey("nomics")}&ids=BTC&interval=1d&convert=USD&per-page=100&page=1'


def load_data(btc_data, look_back):
    data_raw = btc_data.values 
    data = []
    
    # create all possible sequences of length 
    for index in range(len(data_raw) - look_back): 
        data.append(data_raw[index: index + look_back])
    
    data = np.array(data);
    test_set_size = int(np.round(0.2*data.shape[0]));
    train_set_size = data.shape[0] - (test_set_size);
    
    x_train = data[:train_set_size,:-1,:]
    y_train = data[:train_set_size,-1,:]
    
    x_test = data[train_set_size:,:-1]
    y_test = data[train_set_size:,-1,:]
    
    return [x_train, y_train, x_test, y_test]



# model

input_dim = 1
hidden_dim = 32
num_layers = 2 
output_dim = 1


# model class
class LSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers, output_dim):
        super(LSTM, self).__init__()

        self.hidden_dim = hidden_dim

        # Number of hidden layers
        self.num_layers = num_layers

        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)

        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        # Initialize hidden state
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).requires_grad_()

        # Initialize cell state
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).requires_grad_()

        #detach backpropagation
        out, (hn, cn) = self.lstm(x, (h0.detach(), c0.detach()))

        # step the hidden states
        out = self.fc(out[:, -1, :]) 
        return out

def run(source):
    df_btc=pd.read_csv(source + ".csv", parse_dates=True,index_col=0)
    last_date = df_btc.index[-1]
    scaler = MinMaxScaler(feature_range=(-1, 1))
    df_btc['Price'] = scaler.fit_transform(df_btc['Price'].values.reshape(-1,1))


    look_back = 30 
    x_train, y_train, x_test, y_test = load_data(df_btc, look_back)

    x_train = torch.from_numpy(x_train).type(torch.Tensor)
    x_test = torch.from_numpy(x_test).type(torch.Tensor)
    y_train = torch.from_numpy(y_train).type(torch.Tensor)
    y_test = torch.from_numpy(y_test).type(torch.Tensor)



    model = LSTM(input_dim=input_dim, hidden_dim=hidden_dim, output_dim=output_dim, num_layers=num_layers)

    loss_fn = torch.nn.MSELoss()

    optimiser = torch.optim.Adam(model.parameters(), lr=0.01)

    # Train model
    num_epochs = 200
    hist = np.zeros(num_epochs)

    # Number of steps to unroll
    seq_dim =look_back-1  

    for t in range(num_epochs):
        # Forward pass
        y_train_pred = model(x_train)

        loss = loss_fn(y_train_pred, y_train)
        if t % 10 == 0 and t !=0:
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
    y_train_pred = scaler.inverse_transform(y_train_pred.detach().numpy())
    y_train = scaler.inverse_transform(y_train.detach().numpy())
    y_test_pred = scaler.inverse_transform(y_test_pred.detach().numpy())
    y_test = scaler.inverse_transform(y_test.detach().numpy())

    # calculate root mean squared error
    trainScore = math.sqrt(mean_squared_error(y_train[:,0], y_train_pred[:,0]))
    print('Train Score: %.2f RMSE' % (trainScore))
    testScore = math.sqrt(mean_squared_error(y_test[:,0], y_test_pred[:,0]))
    print('Test Score: %.2f RMSE' % (testScore))

    # Visualising the results
    # figure, axes = plt.subplots(figsize=(15, 6))
    # axes.xaxis_date()

    # axes.plot(df_btc[len(df_btc)-len(y_test):].index, y_test, color = 'green', label = 'Real BTC Price')
    # axes.plot(df_btc[len(df_btc)-len(y_test):].index, y_test_pred, color = 'blue', label = 'Predicted BTC Price')

    predicted_price = y_test_pred[-1][0] #post this data to website

    #when time is 5 minutes, get actual price, and send the prediction to api
    counter = 0
    predictDate = last_date.strftime("%Y-%m-%d %H:%M:%S")
    while True:
        dateString = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if predictDate < dateString:
            if counter == 0:
                counter = counter + 1
                try:
                    r = requests.get(url = NOMICS_URL) 
                    json_data  = r.json()
                    actual_price = format(float(json_data[0]['price']), ".6f")
                    rate = format(((float(predicted_price) - float(actual_price)) /float(predicted_price)), ".6f")
                    trend = "Neutral"
                    if(float(rate) > 0):
                        trend = "Up"
                    elif(float(rate) < 0):
                        trend = "Down"
                    print(f"time: {dateString} predicted: {predicted_price} actual price: {actual_price} rate: {rate}")
                    timestamp = datetime.datetime.now().timestamp()
                    apiURL = 'https://bitcoinpriceprediction-mu.herokuapp.com/api/bitcoin'
                    myobj = {
                        'date': dateString,
                        'timestamp': timestamp, 
                        'price':actual_price, 
                        'prediction':predicted_price, 
                        'rate': rate,
                        'trend': trend
                        }

                    x = requests.post(apiURL, data = myobj)

                    print(x.text)

                    break
                except:
                    print("Error")
                    break


# run("nomics")
    # plt.title('BTC Price Prediction')
    # plt.xlabel('Time')
    # plt.ylabel('BTC Price')
    # plt.legend()
    # plt.savefig('BTC_pred.png')
    # plt.show()