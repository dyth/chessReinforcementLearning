#!/usr/bin/env python
"""
Value Network based on Giraffe
"""
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F


# save floating point values
Tensor = FloatTensor

# if gpu use cuda
use_cuda = torch.cuda.is_available()
FloatTensor = torch.cuda.FloatTensor if use_cuda else torch.FloatTensor
LongTensor = torch.cuda.LongTensor if use_cuda else torch.LongTensor
ByteTensor = torch.cuda.ByteTensor if use_cuda else torch.ByteTensor


class evalNet(nn.Module):
    """
    Value Network Layers, Architecture and forward pass
    """
    def __init__(self):
        'initialise all the layers and activation functions needed'
        super(Net, self).__init__()
        # fully connected first layer
        self.fc1 = nn.Linear(368, 95)

        # sliced first layer
        self.fc1_1 = nn.Linear(24, 24)
        self.fc1_2 = nn.Linear(80, 17)
        self.fc1_3 = nn.Linear(136, 34)
        self.fc1_4 = nn.Linear(128, 20)
        
        self.fc2 = nn.Linear(95, 64)
        self.fc3 = nn.Linear(64, 1)
        self.relu = nn.ReLU()
        self.tanh = nn.Tanh()
    
    def forward(self, inputLayer):
        'compute the forward pass of the network'
        # fully connected first layer
        #out = self.fc1(inputLayer)
        
        # slice input layer
        inputLayer_1 = inputLayer.narrow(0, 0, 24)
        inputLayer_2 = inputLayer.narrow(0, 24, 104)
        inputLayer_3 = inputLayer.narrow(0, 104, 240)
        inputLayer_4 = inputLayer.narrow(0, 240, 368)

        # output slices
        out_1 = self.fc1_1(inputLayer_1)
        out_2 = self.fc1_2(inputLayer_2)
        out_3 = self.fc1_3(inputLayer_3)
        out_4 = self.fc1_4(inputLayer_4)

        # concatenate all outputs
        out = torch.cat((out_1, out_2, out_3, out_4), 0)
        
        # second and third layers, output should be between -1 and +1
        out = self.relu(out)
        out = self.fc2(out)
        out = self.relu(out)
        out = self.fc3(out)
        out = self.tanh(out)
        return out
