#!/usr/bin/env python
"""
Value Network based on Giraffe
"""
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

from weightsToPyTorch import *


# filename of the weights used
filename = "../eval.t7"


class EvalNet(nn.Module):
    """
    Value Network Layers, Architecture and forward pass
    """
    def __init__(self):
        'initialise all the layers and activation functions needed'
        super(EvalNet, self).__init__()

        # sliced first layer
        self.fc1_1 = nn.Linear(24, 24)
        self.fc1_2 = nn.Linear(80, 17)
        self.fc1_3 = nn.Linear(136, 34)
        self.fc1_4 = nn.Linear(128, 20)

        # second and third layers
        self.fc2 = nn.Linear(95, 64)

        self.fc2a = nn.Linear(64, 640)
        self.fc2b = nn.Linear(640, 640000)
        self.fc2c = nn.Linear(640000, 640)
        self.fc2d = nn.Linear(640, 64)

        self.fc3 = nn.Linear(64, 1)

        
    def forward(self, inputLayer):
        'compute the forward pass of the network'
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
        out = F.relu(self.fc2a(out))
        out = F.relu(self.fc2b(out))
        out = F.relu(self.fc2c(out))
        out = F.relu(self.fc2d(out))
        out = F.tanh(self.fc3(out))
        return out


def create_cuda_EvalNet():
	'return new EvalNet instance using CUDA'
	model = EvalNet()
	return model.cuda()


def load_giraffe_weights(network):
	'load weights trained by original Lua / C++ Giraffe'
	network.load_state_dict(read_parameters(filename))


def forward_pass(network, x):
	'do a forward pass of the network'
	return network(Variable(x)).data[0][0]


if __name__ == "__main__":
	'create network and verify it works with previous giraffe weights'
	evalNet = EvalNet()
	# verification: load weights and get output
	print forward_test(evalNet)
	load_giraffe_weights(evalNet)
	forward_pass(torch.FloatTensor(1, 368), evalNet)
	print forward_test(evalNet)

	# save weights
	#torch.save(evalNet.state_dict(), "weights.t7")
