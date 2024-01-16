import torch
from icecream import ic

torch.manual_seed(7)
t = torch.randn(1, 1, 1, 10)
sq = torch.squeeze(t)

ic(t, t.size())
ic(sq, sq.size())
