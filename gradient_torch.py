import torch
import torch.nn as nn

x = torch.tensor([[1],[2],[3],[4]], dtype=torch.float32)
y = torch.tensor([[2],[4],[6],[8]], dtype=torch.float32)

x_Test = torch.tensor([5],dtype=torch.float32)

n_samples, n_features =x.shape 

input_size = n_features
output_size = n_features
# model =nn.Linear(input_size, output_size)

class LinearRegression(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegression, self).__init__()
        self.lin = nn.Linear(input_dim, output_dim)
    def forward(self,x):
        return self.lin(x)

model = LinearRegression(input_size, output_size)

print(f'Prediction before training: f(5) = {model(x_Test).item():.3f}')

#training
learning_rate = 0.01
n_iters = 100

loss = nn.MSELoss()

optimizer = torch.optim.SGD(model.parameters(),lr = learning_rate)


for epoch in range(n_iters):
    #predictions forward pass
    y_pred = model(x)

    #loss
    l = loss(y, y_pred)

    #gradient = backward pass
    l.backward() #gradient of backward dl/dw

    #update weights
    optimizer.step()

    #zero gradients
    optimizer.zero_grad()

    if epoch % 10 == 0:
        [w,b] = model.parameters()
        print(f'epoch {epoch+1}: w = {w[0][0].item():.3f}, loss = {l:.8f}')

print(f'Prediction after training: f(5) = {model(x_Test).item():.3f}')