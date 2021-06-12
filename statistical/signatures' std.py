def Versality(pheno,geno):
    versa_dict = {} # dictionary that use phenotype sequence that has length 5 as key and the std of the sequence as value

    for i, e in enumerate(pheno): # run through all the phenotype
        sig = []

        for z in range(len(e)): # run through each site of the phenotype

            # these are used to create the length 5 sequence, for the first two and last two sites and 'E' as end
            #in order to keep them in the middle
            if z == 0:
                sequ_5 = str('EE'+e[z])
#             elif z == 1:
#                 sequ_5 = str('E'+e[z])
#             elif len(e)-z == 2:
#                 sequ_5 = str(e[z]+'E')
            elif len(e)-z == 1:
                sequ_5 = str(e[z]+'EE')
            else:
                sequ_5 = str(e[z])
            sig.append(sequ_5)
        key = ''.join(sig)
        versa_dict[key] = geno [i]

    return versa_dict
