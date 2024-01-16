import torch
from icecream import ic

t = ic(torch.randn(7, 7))
m = torch.randn(1, 7)

ic(t @ torch.transpose(m, 0, 1))