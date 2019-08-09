import torch.nn as nn
import torch.nn.functional as F 

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        # input has one channel and we are outputting 3 channels
        self.conv1 = nn.Conv2d(1,3,3)
        self.conv2 = nn.Conv2d(3,3,3)
        # The image dimention will change from (24,14) to (20,10)
        # after 2 conv2d layers
        self.fc1 = nn.Linear(20*10*3,108)
        # There are total 36 classes
        self.fc2 = nn.Linear(108,36)

    def forward(self, x):
        # sequance of convolutional layers with relu activation
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        # flatten the image input
        x = x.view(-1, 20*10*3)
        # 1st hidden layer with relu activation
        x = F.relu(self.fc1(x))
        # output-layer
        x = self.fc2(x)
        return x