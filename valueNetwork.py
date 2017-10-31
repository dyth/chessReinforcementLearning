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
        super(Net, self).__init__()
        self.fc1 = nn.Linear(368, 95)
        #self.fc1_1 = nn.Linear(24, 24)
        #self.fc1_2 = nn.Linear(80, 17)
        #self.fc1_3 = nn.Linear(136, 34)
        #self.fc1_4 = nn.Linear(128, 20)
        
        self.fc2 = nn.Linear(95, 64)
        self.fc2 = nn.Linear(64, 1)
        self.relu = nn.ReLU()
        self.tanh = nn.Tanh()
    
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.relu(out)
        out = self.fc3(out)
        out = self.tanh(out)
        return out
