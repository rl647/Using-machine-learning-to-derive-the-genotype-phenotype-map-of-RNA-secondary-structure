import RNA
import random
Base = ['A','U','C','G']

'''for samples of genotypes with certaion length'''
def get_random_string(length,base=Base):
    result_str = ''.join(random.choice(base) for i in range(length))
    return result_str
notation = []
gp_original = {}
while len(notation)<10000:
    geno = get_random_string(L)# L=lengths of sequence
    (pheno,mfe) = RNA.fold(geno)
    if pheno in notation or list(pheno).count('(') == 0:
        pass

    else:
        notation.append(pheno)
        gp_original[geno] = pheno


'''exhaustive enumeration of all genotypes with length L'''
def permutation(base=Base, n=L):
    sequence = []
    if n == 0:
        return [[]]
    else:
        for i in range(len(Base)):
            for t in permutation(base, n-1):
                sequence.append([Base[i]]+t)
    return sequence
