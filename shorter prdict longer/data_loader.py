import random
import numpy as np
import json

def data_loader(filename,extra_length,n,size):
    f = open(filename)# open the file the contain the mean neutral mutaion of each phtnotype at each site
    added_side={}
    k_note = {}

    versa_dict = {}
    for line in f:
        s = line.strip().split('\t')
        if list(s[0]).count('(') >= 1:
            s1 = json.loads(s[1])
            versa_dict[s[0]] = s1


    f.close()
    if len(versa_dict)<1000:
        pass
    else:
        versa_dict=dict(random.sample(list(versa_dict.items()),size))


    one_of_k = {}

    if extra_length != 0:

        for i in range(extra_length+1):
            for key,val in versa_dict.items():
                x = list(key)
#                 y = val[:]
                for t, e in enumerate(x):
                    if e == '.' :
                        x[t] = [1,0,0]
#                         y[t] = val[t]/3
                    else:
                        x[t] = [0,0,1]

                y = val[:]
                for w in range(i):
                    if w==0 and x[0] != [1,0,0]:
                        y.insert(0,1.5)
                    else:
                        y.insert(0,2.7)
                for q in range(extra_length-i):
                    if q==0 and x[-1] != [1,0,0]:
                        y.append(1.5)
                    else:
                        y.append(2.7)
                if i!=0:
                    x.insert(0, i*[0,1,0])
                x += (extra_length-i)*[[0,1,0]]


                if str([item for sublist in x for item in sublist]) not in added_side.keys():
                    one_of_k[str(x)] = y  #conver notation "(" and ")" to "*"
                    k_note[str([item for sublist in x for item in sublist])] = key

                    added_side[str([item for sublist in x for item in sublist])] =[i,n]

                elif str([item for sublist in x for item in sublist]) in added_side:
                    rd = [0,1]
                    rdc = random.choice(rd)
                    if rdc == 1:
                        one_of_k[str(x)] = y  #conver notation "(" and ")" to "*"
                        k_note[str([item for sublist in x for item in sublist])] = key

                        added_side[str([item for sublist in x for item in sublist])] =[i,n]

    else:
        for key,val in versa_dict.items():
            x = list(key)
            for t, e in enumerate(x):

                if e == '.' :
                    x[t] = [1,0,0]
#                     y[t] = val[t]/3
                else:
                    x[t] = [0,0,1]
            one_of_k[str(x)] = val  #conver notation "(" and ")" to "*"
            k_note[str([item for sublist in x for item in sublist])] = key


#     x1 = []
#     y1 = []
#     for key, val in one_of_k.items():
#         x1.append(key)
#         y1.append(val)

#     for i, e in enumerate(x1):
#         x1[i] = json.loads(e)

#     for i, e in enumerate(x1):
#         x1[i] = [item for sublist in e for item in sublist]

#     x1=np.array(x1)
#     y1=np.array(y1)

    return k_note, added_side,one_of_k
