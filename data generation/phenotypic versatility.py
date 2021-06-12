import numpy as np
Base = ['A','U','C','G']
def get_phenotype_neutral_mutations(merged_notation,dot_bracket_dict,changed_frequency_final,n):
    frequency = {}
    frequency_list=[]
    notation_changed_frequency = {}
    def get_keys(d,value):
        return [k for k,v in d.items() if v == value]
    for i in range(len(merged_notation)):
        sequence = get_keys(dot_bracket_dict,merged_notation[i])
        changed_times = []
        for t in sequence:
            if len(changed_times)==0:
                changed_times = np.array(changed_frequency_final[t])
            else:
                changed_times = np.array(changed_times )
                changed_times += np.array(changed_frequency_final[t])
        notation_changed_frequency[merged_notation[i]]= (np.array(changed_times)/len(sequence)).tolist()

        if i % 100 == 0:
            print(100*i/len(merged_notation),'%')

    return notation_changed_frequency
