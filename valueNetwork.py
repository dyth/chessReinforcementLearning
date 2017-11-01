#!/usr/bin/env python
"""
Value Network based on Giraffe
"""
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


# if gpu use cuda
use_cuda = torch.cuda.is_available()
FloatTensor = torch.cuda.FloatTensor if use_cuda else torch.FloatTensor
Tensor = FloatTensor
LongTensor = torch.cuda.LongTensor if use_cuda else torch.LongTensor
ByteTensor = torch.cuda.ByteTensor if use_cuda else torch.ByteTensor


class EvalNet(nn.Module):
    """
    Value Network Layers, Architecture and forward pass
    """
    def __init__(self):
        'initialise all the layers and activation functions needed'
        super(EvalNet, self).__init__()
        # fully connected first layer
        self.fc1 = nn.Linear(368, 95)

        # sliced first layer
        self.fc1_1 = nn.Linear(24, 24)
        self.fc1_2 = nn.Linear(80, 17)
        self.fc1_3 = nn.Linear(136, 34)
        self.fc1_4 = nn.Linear(128, 20)

        # second and third layers
        self.fc2 = nn.Linear(95, 64)
        self.fc3 = nn.Linear(64, 1)

        
    def forward(self, inputLayer):
        'compute the forward pass of the network'
        # fully connected first layer
        #out = F.relu(self.fc1(inputLayer))
        
        # slice input layer
        out_1 = inputLayer.narrow(1, 0, 24)
        out_2 = inputLayer.narrow(1, 24, 80)
        out_3 = inputLayer.narrow(1, 104, 136)
        out_4 = inputLayer.narrow(1, 240, 128)

        # output slices
        out_1 = self.fc1_1(out_1)
        out_2 = self.fc1_2(out_2)
        out_3 = self.fc1_3(out_3)
        out_4 = self.fc1_4(out_4)

        # concatenate all outputs
        out = F.relu(torch.cat((out_1, out_2, out_3, out_4), 1))
        
        # second and third layers, output should be between -1 and +1
        out = F.relu(self.fc2(out))
        out = F.tanh(self.fc3(out))
        return out


evalNet = EvalNet()

x = Variable(torch.FloatTensor(1, 368))
outputs = evalNet(x)
print outputs
