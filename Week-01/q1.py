from torch import tensor
import torch
from icecream import ic


def q1():
    t = tensor([1, 2, 3])
    t = ic(t.reshape(3, 1))
    t = ic(torch.squeeze(t))
    stack = ic(torch.stack((t, t), dim=1))
    t = ic(torch.unsqueeze(t, 1))




if __name__ == '__main__':
    q1()
