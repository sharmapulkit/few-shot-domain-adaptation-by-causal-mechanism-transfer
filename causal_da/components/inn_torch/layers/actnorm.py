"""
Adopted from https://github.com/chaiyujin/glow-pytorch/blob/master/glow/modules.py .
"""
import torch
import torch.nn as nn

# Type hinting
from typing import Optional
from torch import FloatTensor


class ActNorm(nn.Module):
    """Activation Normalization.
    Initialize the bias and scale with a given mini batch
    so that the output per-channel have zero mean and unit variance for that.
    After initialization, `bias` and `logs` will be trained as parameters.
    """
    def __init__(self, dim: int, scale: float = 1.):
        """
        Parameters:
            dim: dimension of the input.
            scale: a coefficient on the scaling parameter.
        """
        super().__init__()
        # register mean and scale
        size = [1, dim]
        self.register_parameter("bias", nn.Parameter(torch.zeros(*size)))
        self.register_parameter("logs", nn.Parameter(torch.zeros(*size)))
        self.dim = dim
        self.scale = float(scale)
        self.initializeed = False
        # self.bias = self.bias.to(torch.device("cuda"))
        # self.bias = torch.tensor(self.bias, device=torch.device('cuda'))

    def initialize_parameters(self, x: FloatTensor):
        """Data-dependent initialization of the parameters.
        The parameters are treated as trainable parameters (independent of the data) after the initialization.

        Parameters:
            x: input tensor.
        """
        if not self.training:
            return
        # print("Devices:x", x.device, "::bias:", self.bias.device)
        # assert x.device == self.bias.device
        with torch.no_grad():
            bias = _mean(x.clone(), dim=0, keepdim=True)
            variance = _mean((x.clone() - bias)**2, dim=0, keepdim=True)
            logs = torch.log(self.scale / (torch.sqrt(variance) + 1e-6))
            self.bias.data.copy_(bias.data)
            self.logs.data.copy_(logs.data)
            self.initializeed = True

    def forward(self, x: FloatTensor) -> FloatTensor:
        """Perform forward propagation.

        Parameters:
            x: input tensor.
        """
        if not self.initializeed:
            self.initialize_parameters(x)
        # center and scale
        # print("Devices:x", x.device, "::bias:", self.bias.device, "::exp:", torch.exp(self.logs).device)
        # x = x.to('cuda')
        x = (x - self.bias) * (torch.exp(self.logs))
        return x

    def inv(self, x: FloatTensor) -> FloatTensor:
        """Perform the inverse computation in a batch.

        Parameters:
            x: input tensor.
        """
        # scale and center
        x = x * torch.exp(-self.logs) + self.bias
        return x


def _mean(tensor: FloatTensor,
          dim: Optional[int] = None,
          keepdim: bool = False) -> FloatTensor:
    """Utility function to compute the average."""
    if dim is None:
        # mean all dim
        return torch.mean(tensor)
    else:
        if isinstance(dim, int):
            dim = [dim]
        dim = sorted(dim)
        for d in dim:
            tensor = tensor.mean(dim=d, keepdim=True)
        if not keepdim:
            for i, d in enumerate(dim):
                tensor.squeeze_(d - i)
        return tensor
