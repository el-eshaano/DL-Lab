import torch
import numpy as np
from icecream import ic

a = np.array([1, 2, 3])
t = ic(torch.tensor(a))
a = ic(np.array(t))