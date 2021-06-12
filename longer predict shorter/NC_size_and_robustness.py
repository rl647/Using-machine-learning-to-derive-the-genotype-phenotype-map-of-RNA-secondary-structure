import numpy as np

def NC_size_robustness(std_dict, note_dict,L):
    '''
        std_dict is a standard deviation of phenotype versality,
        note_dict is versality of phenotyoe
    '''
    if L == 12:
        alpha = 0.43
    elif L == 15:
        alpha =0.46
    elif L==17:
        alpha = 0.48
    else:
        alpha=0.68*(1-np.exp(-0.079*L))

    sNC  = {}
    Robust = {}
    for keys,vals in std_dict.items():
        s1 = note_dict[keys]  # versatility value of phenotypes sequence
        t1 = vals # std of phenotypes sequence
        s_NC = 1
        ro = 0

        for i, e in enumerate(t1):
            ro+=s1[i]
            if list(keys)[i] == '.':
                s_NC *= min(1+s1[i]+alpha*e, 4)
            else:
                s_NC *= min(1+s1[i]+alpha*e, 2)
        Robust[keys] = ro/3/L
        sNC[keys] = s_NC




    return sNC, Robust
