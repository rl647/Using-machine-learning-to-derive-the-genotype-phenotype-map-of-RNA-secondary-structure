def sig_freq(pheno,geno):
    versa_dict = {} # dictionary that use phenotype sequence that has length 5 as key and the central neutral mutation of the sequence as value
    signature_freq = {}# save signature as key and the amount of times it appears as value
    for i, e in enumerate(pheno): # run through all the phenotype

        for z in range(len(e)): # run through each site of the phenotype

            muta = np.array([geno[i][z],1])# array that contain site neutral mutation and 1 will be sum in order to calculate mean value

            # these are used to create the length 5 sequence, for the first two and last two sites and 'E' as end
            #in order to keep them in the middle
            if z == 0:
                sequ_5 = str('EE'+e[z:z+3])
            elif z == 1:
                sequ_5 = str('E'+e[z-1:z+3])
            elif len(e)-z == 2:
                sequ_5 = str(e[z-2:z+2]+'E')
            elif len(e)-z == 1:
                sequ_5 = str(e[z-2:z+1]+'EE')
            else:
                sequ_5 = str(e[z-2:z+3])

            if sequ_5 in versa_dict:
                versa_dict[sequ_5] = versa_dict[sequ_5]+muta #if the dictionary alreay contained the sequence,add the value
            else:
                versa_dict[sequ_5] = muta # if not, create a new key and value

    versequ_list = list(versa_dict.keys())#get all the key of the dictionary
    for i in versequ_list:
        signature_freq[i] = versa_dict[i][1]
        versa_dict[i] = versa_dict[i][0]/versa_dict[i][1]# for the key in the dictionary, divided the value by the amount of times it appeared
    return versa_dict, signature_freq
