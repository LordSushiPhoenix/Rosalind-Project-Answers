dna = "TACAAGAAGTCGAGTCACCTCCTACCACGGCCGTAGCCGGCTGTGGTGTGTTTTACAAGACTTTAACTACGTGTTAGCGCCAGGTGTGGCGCCTTCGTATGTTATCGTAGCCCAGATAGTGTTTAACCCCTGGGATTTCATACGTTTCTTGCATCGGCATTACGACAGAAAGTGGGGGGCCTAATCTATGACACTGAATCATGGATTCATGTTTCGACCTTTCCACCACGTTGGTTGCTCGTGTCCTTTGGATCTCTCGGCTCACCATGATAGAGACGATGTACCGTAAATAGCTCATCTGATGTACTGTTCTATGTTTGCTTCCGCAGTTGCCGTTATGTCGGTATGCGGGCTATCCGCAAGACTACTTGTTGGCCACATCTTGTTATACTTGACCTCCCTTTGGGTATTTGGGAGTAGAGGAATCATGCACCACGTTGAGCCCTAAGCAGGAAGGCACAGTTTGGTGTCCGTATTTACCCATCATGTAAATACTACGAAGCCAAGAACACCTAGCGCGGCCAGGTGCACATTTTCACCGGGTAGCGGCTGTGCCCATCGGGGTGGTGGTAGATGTTAATGTCACTACTCTGCAATCAATTCGCAAGGCAGACGACTAAAAGTCATGCTGATTTATCGTGACCATCTACAAGATATTGCCACATTTTGGAGCGTGAAAGCGAACCTTCGCGCACAACGCCGTTCCGTCGTACCGGTGCGCTTCAACCGGCGGTCATTATATCTCGGCACGTTTAGGGATCTTCTCGTGGGATAACGATCAATGCTCAGTGAATGGCTAACTTACTGAGAAGCAAGCGATTCCTCACATAGTATGTCGATTTATGACCTTTTGACTCCGG"
rna =""
print(len(dna))
for i in range((len(dna)-1), -1, -1):
    if dna[i] == 'A':
        rna += 'T'
    elif dna[i] == 'T':
        rna += 'A'
    elif dna[i] == 'G':
        rna += 'C'
    elif dna[i] == 'C':
        rna += 'G'

print(len(rna))
print('complement is: %s' % rna)