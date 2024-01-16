import torch
from icecream import ic

a = torch.randn(2, 3)
b = torch.randn(2, 3)

print(a)
ic(torch.max(a))
ic(torch.min(a))
ic(torch.argmax(a))
ic(torch.argmin(a))

