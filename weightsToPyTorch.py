#!/usr/bin/env python
"""
convert weights from the torch .t7 format to the dictionary used in PyTorch
"""
import re, torch

def read_parameters():
    'read the parameters in the file eval.t7 and convert to PyTorch weights'
    weights = []
    with open("eval.t7") as f:
        content = [x.strip() for x in f.readlines()] 
        for c in content:
            # regex to get all valid rows with type: string of float list
            if ('.' in c) and ('nn' not in c) and ('torch' not in c):
                weights.append(c.split(' '))
    # convert to list of floating point values
    weights = [[float(w) for w in weight] for weight in weights]

    # lookup weight size to PyTorch representation
    sizeToLayer = {
        24.0: "fc1_1",
        17.0: "fc1_2",
        34.0: "fc1_3",
        20.0: "fc1_4",
        64.0: "fc2",
        1.0: "fc3"
    }

    # generate parameters -- PyTorch weight dictionary
    parameters = {}
    for w in weights:
        if w[1] in sizeToLayer:
            key = sizeToLayer[w[1]]
            # if 1.0, then it is a bias tensor. otherwise it is a weight vector
            if w[0] == 1.0:
                key += '.bias'
                weightVector = torch.FloatTensor(w[2:])
            else:
                # resize the tensor to pytorch 2D format
                key += '.weight'
                size = int(len(w[3:]) / w[1])
                weightVector = torch.FloatTensor(w[3:]).resize_(int(w[1]), size)
            parameters[key] = weightVector
            
    return parameters
