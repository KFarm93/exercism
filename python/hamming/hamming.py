def distance(strand1, strand2):
    mutations = 0
    idx = 0
    if len(strand1) != len(strand2):
        return 'Sequences not of equal length'
    else:
        for nucleotide in strand1:
            if nucleotide != strand2[idx]:
                print "%s is not equal to %s" % (nucleotide, strand2[idx])
                mutations += 1
                idx += 1
            else:
                idx += 1
    return mutations


distance(['A', 'T', 'T', 'G', 'C'], ['G', 'A', 'A', 'T', 'C'])
