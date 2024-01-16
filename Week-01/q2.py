import torch
from icecream import ic


def q2():
    x = torch.randn(2, 3, 5)
    x.size()
    ic(torch.permute(x, (2, 0, 1)).size())


if __name__ == '__main__':
    q2()
