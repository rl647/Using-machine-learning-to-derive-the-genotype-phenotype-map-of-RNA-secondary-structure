import random
import RNA
import numpy as np
Base = ['A','U','C','G']
def get_genotype_number_of_neutral_mutations(Base,dot_bracket_dict):
    a = []
    for key, val in dot_bracket_dict.items():
        a.append(key)
    changed_frequency_final={}
    for i in range(len(a)):
        changed_frequency_moment = []
        for t in range(len(a[i])):
            RES_Base = Base[:]
            change = 0
            for x in range(3):
                if a[i][t] in RES_Base:
                    RES_Base.pop(RES_Base.index(a[i][t]))
                copy_a = list(a[i])
                copy_a[t]=RES_Base[x]
                copy_a = "".join(copy_a)
                if str(copy_a) in dot_bracket_dict.keys():
                    if dot_bracket_dict[a[i]] == dot_bracket_dict[str(copy_a)] :
                        change+=1
                else:
                    (ss,mfe) = RNA.fold(str(copy_a))
                    if ss == dot_bracket_dict[a[i]]:
                        change+=1
            changed_frequency_moment.append(change)
        if i % 10000 == 0 :
            print(100*i/len(a),'%')

        changed_frequency_final[a[i]] = changed_frequency_moment
    return changed_frequency_final
