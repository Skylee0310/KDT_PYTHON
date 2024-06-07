import torch
import torch.nn as nn
import torch.nn.functional as F

class CNN(nn.Module) :
    def __init__(self) :
        super().__init__()
        self.conLayer = nn.Conv2d(in_channels=3, out_channels=25, kernel_size = 3, )
        self.conLayer2 = nn.Conv2d(in_channels=25, out_channels=10, kernel_size = 3)
        self.pool1 = nn.MaxPool2d(2, 2) 
        self.fc1 = nn.Linear(10*14*14, 1000)
        self.fc2 = nn.Linear(1000, 500)
        self.fc3 = nn.Linear(500, 250)
        self.fc4 = nn.Linear(250, 125)
        self.fc5 = nn.Linear(125, 60)
        self.fc6 = nn.Linear(60, 2)

    def forward(self, x) :
        x = self.conLayer(x)
        x = F.relu(x)
        x = self.pool1(x)
        x = self.conLayer2(x)
        x = F.relu(x)
        x = self.pool1(x)
        x = x.view(-1, 10*14*14) 
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.relu(x)
        x = self.fc4(x)
        x = F.relu(x)
        x = self.fc5(x)
        x = F.relu(x)        
        x = self.fc6(x)

        return x