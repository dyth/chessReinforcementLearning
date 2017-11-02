#!/usr/bin/env python
"""
convert weights from the torch .t7 format to the dictionary used in PyTorch
"""
import re
import torch
from torch.utils.serialization import load_lua


# get all valid rows containing weights
weights = []
with open("eval.t7") as f:
    content = [x.strip() for x in f.readlines()] 
    for c in content:
        # some good old regex for determining whether the 
        if ('.' in c) and ('nn' not in c) and ('torch' not in c):
            weights.append(c.split(' '))

weights = [[float(w) for w in weight] for weight in weights]
print "number of weight tensors:", len(weights)
for i, w in enumerate(weights):
    print i, len(w), w[0:4]
