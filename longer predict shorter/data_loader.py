import json
import numpy as np
import random 
def data_loader(filename,extra_length):
    f = open(filename)  # open the file the contain the mean neutral mutaion of each phtnotype at each site
    versa_dict = {}

    k_note = {}
    for line in f:
        s = line.strip().split('\t')
        if list(s[0]).count('(') >= 1:
            s1 = json.loads(s[1])
            versa_dict[s[0]] = s1

    f.close()

    one_of_k = {}
    x_y = [[],[]]
    for key,val in versa_dict.items():
        x = list(key)
        y = val[:]
        for t, e in enumerate(x):
            if e == '(' :
                x[t] = [0.,1.,0.]
            elif e == ')':
                x[t] = [0.,0.,1.]
            else:
#                 y[t] = val[t]/3
                x[t] = [1.,0.,0.]
        if extra_length%2 == 0:
            z=int(extra_length/2)
            for i in range(z):
                x.insert(0,[1.,0.,0.])
                x.append([1.,0.,0.])
        else:
            z=int(extra_length/2)
            for i in range(z+1):
                x.insert(0,[1.,0.,0.])
                if i > 0:
                    x.append([1.,0.,0.])
        k_note[str([item for sublist in x for item in sublist])] = key
        one_of_k[str(x)] = y  #conver notation "(" and ")" to "*"
        x_y[0].append(x)
        x_y[1].append(val)

    x1 = sorted(one_of_k, key=one_of_k.get, reverse=True)
    y1 = []
    for i in x1:
        y1.append(one_of_k[i])

    for i, e in enumerate(x1):
        x1[i] = json.loads(e)

    for i, e in enumerate(x1):
        x1[i] = [item for sublist in e for item in sublist]

    x1=np.array(x1)
    y1=np.array(y1)

    return x1, y1, k_note
