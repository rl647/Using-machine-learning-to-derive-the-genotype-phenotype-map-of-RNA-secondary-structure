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


        self.fc1 = nn.Linear(60,90)
#         setattr(self,'fc%i'%i,fc)
        self._set_init(self.fc1)
#         self.fcs.append(fc)
        self.bn1 = nn.BatchNorm1d(90,momentum=0.5)
#         setattr(self,'bn%i'%i,bn)
#         self.bns.append(bn)

        self.fc2 = nn.Linear(90,120)
        self._set_init(self.fc2)
        self.bn2 = nn.BatchNorm1d(120,momentum=0.5)

        self.fc3 = nn.Linear(120,80)
        self._set_init(self.fc3)
        self.bn3 = nn.BatchNorm1d(80,momentum=0.5)

        self.fc4 = nn.Linear(80,40)
        self._set_init(self.fc4)
        self.bn4 = nn.BatchNorm1d(40,momentum=0.5)


        self.predict = nn.Linear(40,20)
        self._set_init(self.predict)

    def _set_init(self, layer):
        init.normal_(layer.weight,mean=0.,std=0.025)
        init.constant_(layer.bias, B_INIT)


    def forward(self, x):

        x = torch.tanh(self.fc1(x))
        x = torch.tanh(self.fc2(x))
        x = torch.tanh(self.fc3(x))
        x = torch.tanh(self.fc4(x))

        x = self.predict(x)

        return x
