def to_rna(dna):
    rna = []
    for nucleotide in dna:
        if nucleotide == 'G':
            nucleotide = 'C'
            rna.append(nucleotide)
        elif nucleotide == 'C':
            nucleotide = 'G'
            rna.append(nucleotide)
        elif nucleotide == 'T':
            nucleotide = 'A'
            rna.append(nucleotide)
        elif nucleotide == 'A':
            nucleotide = 'U'
            rna.append(nucleotide)
    return rna

to_rna(['G', 'A', 'A', 'T', 'C'])
