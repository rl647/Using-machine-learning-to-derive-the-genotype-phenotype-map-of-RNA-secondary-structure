import random
import RNA
import numpy as np

def site_scanning(gp_map, base,n, size):
    pg_map = {}# store the phenotype as key, genotype as value
    map_size = 0
    for key, val in gp_map.items():#key is genotype, val is phenotype

        current_map = {}#store the genotype as key, faster check as hash dict time complexity is 1

        current_map[val] = key


        NC = [key]#Neutral component of phenotype:val

        restart = True#restart the for loop

        site = 0# record the current site of the sequence

        count = 0# count the number of restart loop
        asd = []
        while restart:
            count+=1

            for position, sequence in enumerate(NC):# traverse through the current NC


                num_mutation = 0 # the neutral mutation of current genotype

                genotype = list(sequence)# convert string genotype to list

#                 site = circle%n #the site that genotype should start

#                 print(circle)

                for i in range(n):# traverse from the site of base till the end
                    Res_base = base[:]#copy the value of base and avoid changing it in the future
                    #pop up the base that exist in the current site of the sequence
                    i=int(site+i)%n
                    Res_base.remove(genotype[i])



                    for t in range(3):# traverse through different base

                        mutated_geno = genotype[:]# copy the current genotype

                        sub_base = random.choice(Res_base)# randomly choose one base from the remaining base
                        Res_base.remove(sub_base)#pop up the chosen base
                        mutated_geno[i] = sub_base #subtitue the base of the site
                        mutated_geno = ''.join(mutated_geno)
                        if mutated_geno in current_map:
                            site = (site+1)%n
                            break
                        ss, mfe = RNA.fold(mutated_geno)


                        # if the mutated genotype form the same phenotype and this genotype not in the dictionary
                        if ss == val and mutated_geno not in current_map:
                            current_map[mutated_geno] = val# add the genotype in the list

                            #insert the genotype to the NC so that the next sample will be the successed neutral mutation

                            NC.insert(position+1,mutated_geno)

                            #the number of neutral mutation +1 and later on terminate the loop of this genotype
                            num_mutation+=1
                            site = (site+1)%n# the neutral mutation of site move to the next position
                            break# break the loop of the current site of the genotype
                        elif t == 2:
                            site = (site+1)%n


                    if num_mutation == 1:
                        break# break the loop of current genotype


#                 NC = list(set(NC))

                if len(NC) == size:
                    break#break the loop of current phenotype


            if len(NC) >=size:
                restart = False# stop starting the loop of current phenotype
            elif count >= n:
                restart = False# if the loop has been restarted more than the length of sequence, terminated the loop

        pg_map[val] = NC# add the NN as val, phenotype as key
        if map_size%20 == 0:
            print(100*map_size/len(gp_map), '%')
        map_size += 1
    return pg_map
