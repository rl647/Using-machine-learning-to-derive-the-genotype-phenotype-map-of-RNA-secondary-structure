import torch
from torch import nn
import torch.utils.data as Data
from torch.nn import init

B_INIT = -0.2


class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
#         self.do_bn = batch_normalizatoin
#         self.bn_input = nn.BatchNorm1d(90, momentum=0.5)


        self.fc1 = nn.Linear(120,150)
#         setattr(self,'fc%i'%i,fc)
        self._set_init(self.fc1)
#         self.fcs.append(fc)
        self.bn1 = nn.BatchNorm1d(150,momentum=0.5)
#         setattr(self,'bn%i'%i,bn)
#         self.bns.append(bn)

        self.fc2 = nn.Linear(150, 180)
        self._set_init(self.fc2)
        self.bn2 = nn.BatchNorm1d(180,momentum=0.5)

        self.fc3 = nn.Linear(180,140)
        self._set_init(self.fc3)
        self.bn3 = nn.BatchNorm1d(140,momentum=0.5)

        self.fc4 = nn.Linear(140,100)
        self._set_init(self.fc4)
        self.bn4 = nn.BatchNorm1d(100,momentum=0.5)

        self.fc5 = nn.Linear(100,60)
        self._set_init(self.fc4)
        self.bn4 = nn.BatchNorm1d(60,momentum=0.5)

        self.predict = nn.Linear(60,40)
        self._set_init(self.predict)

    def _set_init(self, layer):
        init.normal_(layer.weight,mean=0.,std=0.009)
        init.constant_(layer.bias, B_INIT)


    def forward(self, x):

        x = torch.tanh(self.fc1(x))
        x = torch.tanh(self.fc2(x))
        x = torch.tanh(self.fc3(x))
        x = torch.tanh(self.fc4(x))
        x = torch.tanh(self.fc5(x))

        x = self.predict(x)

        return x
